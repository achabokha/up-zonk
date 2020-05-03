import { $log, ServerLoader } from "@tsed/common";
import { Server } from "./Server";
import { createConnection } from "typeorm";

async function bootstrap() {
    createConnection({
        type: "mysql",
        host: process.env?.db_host? process.env.db_host : "localhost",
        port: 3306,
        username: process.env?.db_user? process.env.db_user : "catalog",
        password: process.env?.db_password? process.env.db_password : "",
        database: process.env?.db_name? process.env.db_name : "catalog",
        entities: [
            __dirname + "/entities/*.ts"
        ],
        synchronize: false,
        logging: true,
    })
        .then((connection) => {
            // here you can start to work with your entities
            $log.info("typoORM initialized out of DI.");
            console.log("typoORM initialized out of DI.");
        })
        .catch((error) => console.log(error));

    try {
        //$log.info("Load configuration...");
        // TODO: pause everything and load config (sync call!)
        // make load local config from .env file and async...
        let sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
        sleep(0);

        $log.debug("Start server...");
        const server = await ServerLoader.bootstrap(Server);

        await server.listen();
        $log.debug("Server initialized");
    } catch (er) {
        $log.error(er);
    }
}

bootstrap();
