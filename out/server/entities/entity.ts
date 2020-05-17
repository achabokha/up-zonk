import { MaxLength, Property, Required } from "@tsed/common";
import { Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity("product")
export class Product {
    @Property()
    @PrimaryGeneratedColumn({ name: "id" })
    @Required()
    id: number;
 
    @Property()
    @Column({ name: "sku" })
    @MaxLength(255)
    sku: string;
 
    @Property()
    @Column({ name: "name" })
    @Required()
    @MaxLength(255)
    name: string;
 
    @Property()
    @Column({ name: "title" })
    @Required()
    @MaxLength(255)
    title: string;
 
    @Property()
    @Column({ name: "desc" })
    @MaxLength(65535)
    desc: string;
 
    @Property()
    @Column({ name: "price" })
    price: number;
 
    @Property()
    @Column({ name: "date_created" })
    dateCreated: string;
 
    @Property()
    @Column({ name: "date_updated" })
    dateUpdated: string;
 
    @Property()
    @Column({ name: "in_stock" })
    inStock: boolean;
}
