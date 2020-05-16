export interface ProductComponent {
		id: number;
		sku?: string;
		name: string;
		title: string;
		desc?: string;
		price?: number;
		date_created?: string;
		date_updated?: string;
		in_stock?: boolean;
}
