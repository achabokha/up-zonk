import { Component, OnInit } from "@angular/core";
import { ProductService } from '@services/product.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Product } from '@models/product';

@Component({
    selector: "app-product-edit",
    templateUrl: "./product-edit.component.html",
    styleUrls: ["./product-edit.component.scss"],
})
export class ProductEditComponent implements OnInit {
    dataSource: any;

    productName: number;
    productId: string;

    constructor(private productService: ProductService, private activatedRoute: ActivatedRoute) {
        this.activatedRoute.params.subscribe((params: Params) => {
            this.productName = params.productName;
            this.productId = this.activatedRoute.snapshot.queryParams.id;
            this.load();
        });
    }

    ngOnInit(): void {}

    load() {
        this.productService
            .read(this.productId)
            .subscribe((result: Product) => (this.dataSource = Object.entries(result)));
    }
}
