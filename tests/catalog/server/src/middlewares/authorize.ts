import { IMiddleware, Middleware, Req, UseAuth, EndpointInfo, Res } from "@tsed/common";
import { Unauthorized, Forbidden } from "@tsed/exceptions";
import { applyDecorators } from "@tsed/core";

export class User {
    constructor(
        public uuid: string, // 4 char EUE
        public name: string,
        public email: string,
        public roles: string[],
        public allowAnonymous?: boolean
    ) {}

    isInRole(role: string) {
        return !!this.roles.find((r) => r == role);
    }
}

export interface IAuthorizationOptions {
    roles?: string[];
}

export function Authorize(options: string[]): Function {
    return applyDecorators(UseAuth(AuthorizeMiddleware, options));
}

@Middleware()
export class AuthorizeMiddleware implements IMiddleware {
    use(@Req() request: Req, @Res() response: Res, @EndpointInfo() endpoint: EndpointInfo) {
        const options = endpoint.get(AuthorizeMiddleware) || {};
        // console.log("options", options);
        // console.log("Authorized");
        let user: User = request["user"];

        if (!user.allowAnonymous) {
            let allowed = options;
            let found = false;

            allowed.forEach((a) => {
                if (user.roles.find((r) => r == a.trim())) {
                    found = true;
                    return;
                }
            });

            if (!found) {
                throw new Forbidden("Forbidden");
            }
        }
    }
}
