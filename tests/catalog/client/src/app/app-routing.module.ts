import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { environment } from "src/environments/environment";

const routes: Routes = [
    { path: "", redirectTo: "catalog", pathMatch: "full" },
    { path: "catalog", loadChildren: () => import("./modules/catalog/catalog.module").then((m) => m.CatalogModule) },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
