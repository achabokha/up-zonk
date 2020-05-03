import { ProductEditComponent } from "./product-edit/product-edit.component";
import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { ProductDetailsComponent } from "./product-details/product-details.component";
import { CatalogComponent } from "./catalog.component";
import { ProductListComponent } from "./product-list/product-list.component";

const routes: Routes = [
    { path: "", redirectTo: "products", pathMatch: 'full' },
    { path: "products", component: ProductListComponent },
    { path: "products/:productName", component: ProductDetailsComponent },
    { path: "products/:productName/edit", component: ProductEditComponent },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class CatalogRoutingModule {}
