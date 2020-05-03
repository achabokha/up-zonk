import { BodyParams, Controller, Get, Post, PathParams, Put, Delete } from "@tsed/common";
import { Product } from "../entities/product";
import { DataService } from "../services/data-service";
import { Authorize } from "../middlewares/authorize";
import { AllowAnonymous } from "../middlewares/allow-anonymous";

@Authorize(["admin"])
@Controller("/products")
export class ProductsCtrl {
    constructor(private db: DataService) {}

    @AllowAnonymous()
    @Get("/")
    getList(): Promise<Product[]> {
        return this.db.Products.find();
    }

    @AllowAnonymous()
    @Get("/:id")
    get(@PathParams("id") id: number) {
        return this.db.Products.findOne(id);
    }

    @Post("/")
    create(@BodyParams() Product: Product): Promise<Product> {
        return this.db.Products.save(Product);
    }

    @Put("/:id")
    async update(@BodyParams() Product: Product) {
        let r = await this.db.Products.save(Product);
        return r;
    }

    @Delete("/:id")
    async delete(@PathParams("id") id: number) {
        let bt = await this.db.Products.findOne(id);
        await this.db.Products.remove(bt);
    }
}
