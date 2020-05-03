import {
    IMiddleware,
    Middleware,
    Req,
    EndpointInfo,
    UseBefore,
    Res,
    Use,
} from "@tsed/common";
import { applyDecorators } from "@tsed/core";

export function AllowAnonymous(): Function {
    return applyDecorators(UseBefore(AllowAnonymousMiddleware));
}

@Middleware()
export class AllowAnonymousMiddleware implements IMiddleware {
    use(
        @Req() request: Req,
        @Res() response: Res,
        @EndpointInfo() endpoint: EndpointInfo
    ) {
        request["user"].allowAnonymous = true;
        console.log("AllowAnonymous");
    }
}
