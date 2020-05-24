import { MaterialModule } from './../../material-modules';
import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { CatalogRoutingModule } from "./catalog-routing.module";
import { CatalogComponent } from "./catalog.component";
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { ProductEditComponent } from './product-edit/product-edit.component';

import { CustomerComponent } from "./customer/customer-action/customer-action.component";
import { CustomerListComponent } from "./customer/customer-list/customer-list.component";
import { CustomerDetailsComponent } from "./customer/customer-details/customer-details.component";
import { CustomerEditComponent } from "./customer/customer-edit/customer-edit.component";

import { ReactiveFormsModule } from '@angular/forms';
import { FlexLayoutModule } from '@angular/flex-layout';

@NgModule({
    declarations: [CatalogComponent, ProductListComponent, ProductDetailsComponent, ProductEditComponent
    , CustomerComponent, CustomerListComponent, CustomerDetailsComponent, CustomerEditComponent],
    imports: [CommonModule, MaterialModule, ReactiveFormsModule, FlexLayoutModule, CatalogRoutingModule],
})
export class CatalogModule {}
