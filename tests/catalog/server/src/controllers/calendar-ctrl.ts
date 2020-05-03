import { Controller, Get, PathParams, ReturnType, Any } from "@tsed/common";

class Calendar {
    id: string;
    name: string;
}

@Controller("/calendars")
export class CalendarCtrl {
    @Get()
    @ReturnType({type: Any, collectionType: Array})
    async findAll(): Promise<Array<any>> {
        return [
            {
                id: "1",
                name: "test-1",
            },
        ];
    }

    @Get("/:id")
    async findById(@PathParams("id") id: string): Promise<Calendar> {
        return {
            id,
            name: "test-1",
        };
    }
}
