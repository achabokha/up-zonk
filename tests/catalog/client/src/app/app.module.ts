import { MaterialModule } from "./material-modules";
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NavComponent } from "./components/nav/nav.component";
import { FlexLayoutModule } from "@angular/flex-layout";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { BreadcrumbComponent } from "./components/breadcrumb/breadcrumb.component";

import { HttpClientModule } from "@angular/common/http";

@NgModule({
    declarations: [AppComponent, NavComponent, BreadcrumbComponent],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        FlexLayoutModule,
        MaterialModule,
    ],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
