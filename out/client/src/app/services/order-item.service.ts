import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { OrderItem } from '@models/order-item.interface';

@Injectable({
    providedIn: 'root',
})
export class OrderItemsService {
    constructor(private httpClient: HttpClient) {}

    getAll(): Observable<OrderItem[]> {
        return this.httpClient.get<OrderItem[]>('rest/order-items');
    }

    create(item: OrderItem) {
        return this.httpClient.post('rest/order-items', item);
    }

    read(id): Observable<OrderItem>  {
        return this.httpClient.get<OrderItem>('rest/order-items/${id}');
    }

    update(id, item: OrderItem) {
        return this.httpClient.put('rest/order-items/${id}', item);
    }

    delete(id) {
        return this.httpClient.delete('rest/order-items/${id}');
    }
}
