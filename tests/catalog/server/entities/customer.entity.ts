import { MaxLength, Property, Required } from "@tsed/common";
import { Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity("customer")
export class Customer {
    @Property()
    @PrimaryGeneratedColumn({ name: "id" })
    @Required()
    id: number;
 
    @Property()
    @Column({ name: "customerNumber" })
    @Required()
    customerNumber: number;
 
    @Property()
    @Column({ name: "customerName" })
    @Required()
    @MaxLength(50)
    customerName: string;
 
    @Property()
    @Column({ name: "contactLastName" })
    @Required()
    @MaxLength(50)
    contactLastName: string;
 
    @Property()
    @Column({ name: "contactFirstName" })
    @Required()
    @MaxLength(50)
    contactFirstName: string;
 
    @Property()
    @Column({ name: "phone" })
    @Required()
    @MaxLength(50)
    phone: string;
 
    @Property()
    @Column({ name: "addressLine1" })
    @Required()
    @MaxLength(50)
    addressLine1: string;
 
    @Property()
    @Column({ name: "addressLine2" })
    @MaxLength(50)
    addressLine2: string;
 
    @Property()
    @Column({ name: "city" })
    @Required()
    @MaxLength(50)
    city: string;
 
    @Property()
    @Column({ name: "state" })
    @MaxLength(50)
    state: string;
 
    @Property()
    @Column({ name: "postalCode" })
    @MaxLength(15)
    postalCode: string;
 
    @Property()
    @Column({ name: "country" })
    @Required()
    @MaxLength(50)
    country: string;
 
    @Property()
    @Column({ name: "salesRepEmployeeNumber" })
    salesRepEmployeeNumber: number;
 
    @Property()
    @Column({ name: "creditLimit" })
    creditLimit: number;
}
