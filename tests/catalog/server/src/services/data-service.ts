import { AfterRoutesInit, Injectable } from "@tsed/common";
import { TypeORMService } from "@tsed/typeorm";
import { Connection } from "typeorm";
import { Product } from "../entities/product";
import { Customer } from "../entities/customer.entity";


@Injectable()
export class DataService implements AfterRoutesInit {
    private connection: Connection;

    get Products() {
        return this.connection.getRepository(Product);
    }

    get Customers() {
        return this.connection.getRepository(Customer);
    }

    constructor(private typeORMService: TypeORMService) {}

    $afterRoutesInit() {
        this.connection = this.typeORMService.get()!; // get connection by name if need --
    }
}
