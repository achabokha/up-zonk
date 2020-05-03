import { GlobalAcceptMimesMiddleware, ServerLoader, ServerSettings, $log } from "@tsed/common";
import * as bodyParser from "body-parser";
import * as compress from "compression";
import * as cookieParser from "cookie-parser";
import * as methodOverride from "method-override";
import * as proxy from "express-http-proxy";
import { join } from "path";
import AuthenticateMiddleware from "./middlewares/authenticate";
import { CustomLogIncomingRequestMiddleware } from "./middlewares/custom-log-incoming-request";

require("dotenv").config();

const isDev = () => true;

const rootDir = __dirname;

@ServerSettings({
    rootDir,
    acceptMimes: ["application/json"],
    httpPort: 8080,
    mount: {
        "/dashboard/rest": "${rootDir}/controllers/**/*.ts", // support ts with ts-node then fallback to js
    },
    // TODO: fix - TypeORM initialization does not work from here --
    // typeorm: [
    //     {
    //         name: "default",
    //         type: "mysql",
    //         host: "localhost",
    //         port: 3306,
    //         username: "dashboard",
    //         password: "",
    //         database: "dashboard",
    //         synchronize: false,
    //         logging: true,
    //         //  entities: [`${__dirname}/entities/*{.ts,.js}`],
    //         // "migrations": [`${__dirname}/migrations/*{.ts,.js}`],
    //         // "subscribers": [`${__dirname}/subscribers/*{.ts,.js}`],
    //     },
    // ],
    componentsScan: [`${rootDir}/converters/*{.ts,.js}`],
    statics: isDev() ? {} : { "/dashboard": `${rootDir}/../dist/dashboard` },
    logger: {
        level: "DEBUG",
        // requestFields: ["reqId", "method", "url", "headers", "body", "query", "params", "duration"],
    },
})
export class Server extends ServerLoader {
    constructor(settings) {
        super(settings);
    }

    /**
     * This method let you configure the express middleware required by your application to works.
     * @returns {Server}
     */
    public $beforeRoutesInit(): void | Promise<any> {
        this.use(GlobalAcceptMimesMiddleware)
            .use(AuthenticateMiddleware)
            .use(cookieParser())
            .use(compress({}))
            .use(methodOverride())
            .use(bodyParser.json())
            .use(bodyParser.urlencoded({ extended: true }));

        this.set("trust proxy", 1); 
    }

    public $afterRoutesInit(): void | Promise<any> {
        if (isDev()) {
            $log.info("Development environment! Running proxy...");
            this.use("/", proxy("localhost:4200"));
            this.use(CustomLogIncomingRequestMiddleware); // cuts annoying socket-js heartbeat calls (ng serve) --
        }
    }
}
