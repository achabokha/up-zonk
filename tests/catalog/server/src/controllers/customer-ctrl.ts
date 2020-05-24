import { BodyParams, Controller, Get, Post, PathParams, Put, Delete } from "@tsed/common";
import { Customer } from "../entities/customer.entity";
import { DataService } from "../services/data-service";
import { Authorize } from "../middlewares/authorize";
import { AllowAnonymous } from "../middlewares/allow-anonymous";

@Authorize(["admin"])
@Controller("/customers")
export class CustomersCtrl {
    constructor(private db: DataService) {}

    @AllowAnonymous()
    @Get("/")
    getList(): Promise<Customer[]> {
        return this.db.Customers.find();
    }

    @AllowAnonymous()
    @Get("/:id")
    get(@PathParams("id") id: number) {
        return this.db.Customers.findOne(id);
    }

    @Post("/")
    create(@BodyParams() Customer: Customer): Promise<Customer> {
        return this.db.Customers.save(Customer);
    }

    @Put("/:id")
    async update(@BodyParams() Customer: Customer) {
        let r = await this.db.Customers.save(Customer);
        return r;
    }

    @Delete("/:id")
    async delete(@PathParams("id") id: number) {
        let bt = await this.db.Customers.findOne(id);
        await this.db.Customers.remove(bt);
    }
}
