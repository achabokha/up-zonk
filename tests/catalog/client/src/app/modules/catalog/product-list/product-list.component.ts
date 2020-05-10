import { ProductService } from "./../../../services/product.service";
import { Component, OnInit } from "@angular/core";
import { Observable } from "rxjs";
import { MatTableDataSource } from "@angular/material/table";
import { Product } from "@models/product.interface";
import { map } from "rxjs/operators";

@Component({
    selector: "app-product-list",
    templateUrl: "./product-list.component.html",
    styleUrls: ["./product-list.component.scss"],
})
export class ProductListComponent implements OnInit {
    dataSource: MatTableDataSource<Product>;

    // dataSource$: Observable<MatTableDataSource<Product>>;

    displayedColumns: string[] = ["id", "name", "title", "desc"];

    constructor(private productService: ProductService) {}

    ngOnInit(): void {
        this.load();
        
        // this.dataSource$ = this.productService.getAll().pipe(
        //     map((r: Product[]) => (new MatTableDataSource<Product>(r)))
        // );
    }

    load() {
        this.productService
            .getAll()
            .subscribe((r: Product[]) => (this.dataSource = new MatTableDataSource<Product>(r)));
    }

    applyFilter(event: Event) {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();
    }
}
