import {
    LogIncomingRequestMiddleware,
    OverrideProvider,
    Req,
    InjectorService,
    Res,
} from "@tsed/common";

@OverrideProvider(LogIncomingRequestMiddleware)
export class CustomLogIncomingRequestMiddleware extends LogIncomingRequestMiddleware {
    constructor(injector: InjectorService) {
        super(injector);
    }

    protected onLogStart(request: Req): void {
        if (this.canLog(request)) {
            super.onLogStart(request);
        }
    }

    protected onLogEnd(request: Req, response: Res): void {
        if (this.canLog(request)) {
            super.onLogEnd(request, response);
        }
    }

    private canLog(request: Req) {
        let url = request.originalUrl || request.url;
        return !url.startsWith("/sockjs-node/");
    }
}
