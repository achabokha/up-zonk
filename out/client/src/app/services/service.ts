import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from '@models/product.interface';

@Injectable({
    providedIn: 'root',
})
export class ProductService {
    constructor(private httpClient: HttpClient) {}

    getAll(): Observable<Product[]> {
        return this.httpClient.get<Product[]>('rest/products');
    }

    create(item: Product) {
        return this.httpClient.post('rest/products', item);
    }

    read(id): Observable<Product>  {
        return this.httpClient.get<Product>('rest/products/${id}');
    }

    update(id, item: Product) {
        return this.httpClient.put('rest/products/${id}', item);
    }

    delete(id) {
        return this.httpClient.delete('rest/products/${id}');
    }
}
