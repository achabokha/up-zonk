export class Customer {
		id: number;
		customerNumber: number;
		customerName: string;
		contactLastName: string;
		contactFirstName: string;
		phone: string;
		addressLine1: string;
		addressLine2?: string;
		city: string;
		state?: string;
		postalCode?: string;
		country: string;
		salesRepEmployeeNumber?: number;
		creditLimit?: number;
}
