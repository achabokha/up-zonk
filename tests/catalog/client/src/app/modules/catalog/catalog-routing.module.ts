import { ProductEditComponent } from "./product-edit/product-edit.component";
import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { ProductDetailsComponent } from "./product-details/product-details.component";
import { CatalogComponent } from "./catalog.component";
import { ProductListComponent } from "./product-list/product-list.component";
import { CustomerListComponent } from "./customer/customer-list/customer-list.component";
import { CustomerEditComponent } from "./customer/customer-edit/customer-edit.component";
import { CustomerDetailsComponent } from "./customer/customer-details/customer-details.component";

const routes: Routes = [
    { path: "", redirectTo: "products", pathMatch: "full" },
    { path: "products", component: ProductListComponent },
    { path: "products/:productName", component: ProductDetailsComponent },
    { path: "products/:productName/edit", component: ProductEditComponent },
    { path: "customer", component: CustomerListComponent },
    { path: "customer/:customerName", component: CustomerDetailsComponent },
    { path: "customer/:customerName/edit", component: CustomerEditComponent },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class CatalogRoutingModule {}
