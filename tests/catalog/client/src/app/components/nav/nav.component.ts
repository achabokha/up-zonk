import { Component } from "@angular/core";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { Observable } from "rxjs";
import { map, shareReplay } from "rxjs/operators";
import { FormBuilder, FormGroup } from "@angular/forms";

@Component({
    selector: "app-nav",
    templateUrl: "./nav.component.html",
    styleUrls: ["./nav.component.scss"],
})
export class NavComponent {

    // displaying user name and uuid --
    user =  {
        name: 'Kevin Marvin',
        uuid: "MK8I"
    }

    sideClosed = false;

    isHandset$: Observable<boolean> = this.breakpointObserver
        .observe(Breakpoints.Medium)
        .pipe(
            map((result) => result.matches),
            shareReplay()
        );

    constructor(
        private breakpointObserver: BreakpointObserver,
    ) {
        this.isHandset$.subscribe(c => this.sideClosed = c);

    }

    toggleSidenav() {
        this.sideClosed = !this.sideClosed;
    }
}
