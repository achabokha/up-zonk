import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: "root",
})
export class ProductService {
    constructor(private httpClient: HttpClient) {}

    getAll() {
        return this.httpClient.get(`rest/products`);
    }

    create(item) {
        return this.httpClient.post(`rest/products`, item);
    }
 
    update(id, item) {
        return this.httpClient.put(`rest/products/${id}`, item);
    }
    
    read(id) {
        return this.httpClient.get(`rest/products/${id}`);
    }

    delete(id) {
        return this.httpClient.delete(`rest/products/${id}`);
    }
}
