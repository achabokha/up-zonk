import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Customer } from '@models/customer.interface';

@Injectable({
    providedIn: 'root',
})
export class CustomersService {
    constructor(private httpClient: HttpClient) {}

    getAll(): Observable<Customer[]> {
        return this.httpClient.get<Customer[]>('rest/customers');
    }

    create(item: Customer) {
        return this.httpClient.post('rest/customers', item);
    }

    read(id): Observable<Customer>  {
        return this.httpClient.get<Customer>('rest/customers/${id}');
    }

    update(id, item: Customer) {
        return this.httpClient.put('rest/customers/${id}', item);
    }

    delete(id) {
        return this.httpClient.delete('rest/customers/${id}');
    }
}
