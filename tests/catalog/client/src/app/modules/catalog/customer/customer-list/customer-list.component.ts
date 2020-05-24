import { Component, OnInit, ViewChild } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { MatTableDataSource } from "@angular/material/table";
import { MatSort } from "@angular/material/sort";
import { MatPaginator } from "@angular/material/paginator";

import { CustomersService } from "@services/customers.service";
import { Customer } from "@models/customer.interface";


@Component({
    selector: 'app-customer-list',
    templateUrl: './customer-list.component.html',
    styleUrls: ['./customer-list.component.scss'],
})
export class CustomerListComponent implements OnInit {
    dataSource: MatTableDataSource<Customer>;

    @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
    @ViewChild(MatSort, { static: true }) sort: MatSort;

    displayedColumns: string[] = ["id", "customerNumber", "customerName", "contactLastName", "contactFirstName", "phone", "addressLine1", "addressLine2", "city", "state", "postalCode", "country", "salesRepEmployeeNumber", "creditLimit"];

    selectedItem;

    constructor(private customersService: CustomersService, public dialog: MatDialog) {}

    ngOnInit(): void {
        this.load();
    }

    load() {
        this.selectedItem = null;
        this.customersService.getAll().subscribe((r: Customer[]) => {
            this.dataSource = new MatTableDataSource<Customer>(r);
            this.dataSource.sort = this.sort;
            this.dataSource.paginator = this.paginator;
        });
    }

    applyFilter(event: Event) {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();
    }

    selectItem(item) {
        this.selectedItem = item;
    }

    refresh() {
        this.load();
    }

    delete(itemId) {
        this.customersService.delete(itemId).subscribe(
            (r) => {
                this.load();
            },
            (error) => {
                console.log("error deleting", error);
            }
        );
    }
}
