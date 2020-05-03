import { MaterialModule } from './../../material-modules';
import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { CatalogRoutingModule } from "./catalog-routing.module";
import { CatalogComponent } from "./catalog.component";
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { ProductEditComponent } from './product-edit/product-edit.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FlexLayoutModule } from '@angular/flex-layout';

@NgModule({
    declarations: [CatalogComponent, ProductListComponent, ProductDetailsComponent, ProductEditComponent],
    imports: [CommonModule, MaterialModule, ReactiveFormsModule, FlexLayoutModule, CatalogRoutingModule],
})
export class CatalogModule {}
