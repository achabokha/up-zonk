import { Constant, IMiddleware, Middleware, Req, Res } from "@tsed/common";
import { Unauthorized, Forbidden } from "@tsed/exceptions";
import { User } from "./authorize";

@Middleware()
export default class AuthenticateMiddleware implements IMiddleware {
    use(@Req() request: Req,  @Res() response: Res) {
        if (request.hostname == "localhost") {
            // TODO: Insert Kevin's fake identity --
            let user = new User("0001", "Andrejs Chewbacca", "andrejs.chewbacca@secretagents.com", ["user"]);
            request["user"] = user;

        } else {
            let user = new User(
                request.headers["x-uuid"].toString(),
                request.headers["x-name"].toString(),
                request.headers["x-email"].toString(),
                request.headers["x-roles"]
                    ? request.headers["x-roles"].toString().split(",").map(item => item.trim())
                    : null
            );

            if(!user.roles) {
                throw new Unauthorized("Unauthorized");
            }

            request["user"] = user;
        }
    }
}
