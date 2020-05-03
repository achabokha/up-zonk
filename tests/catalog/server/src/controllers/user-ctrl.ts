import { Controller, Get, Req } from "@tsed/common";
import { User } from "src/middlewares/authorize";

@Controller("/user-info")
export class UserCtrl {
    @Get("/")
    async UserInfo(@Req() request: Req): Promise<User> {
        return request["user"];
    }
}
