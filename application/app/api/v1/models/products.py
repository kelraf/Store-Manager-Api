products = []
sales = []

class ProductsDetails():

    def __init__(self):
        #A list to store products
        self.products_list = []

    def create_product(self, name, category, buying_price, selling_price, description):
        #A dictionary to store user details
        product_info = {}

        product_info['name'] = name
        product_info['category'] = category
        product_info['buying_price'] = buying_price
        product_info['selling_price'] = selling_price
        product_info['description'] = description
        product_info['id'] = 1 + len(self.products_list)
        self.products_list.append(product_info)
        return True

    def get_all_products(self):
        if len(self.products_list) == 0:
            return "The products list is empty"
        else:
            return self.products_list

    def get_product_by_id(self, id):
        #Loop through the self.product_list to check for the product with the provided id
        for product in self.products_list:
            if product['id'] == id:
                return product
        else:
            return "The product id provided does not exist"