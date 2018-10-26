products = []
sales_list = []
import re

class ProductsDetails():

    def __init__(self):
        #A list to store products
        self.products_list = products


    def create_product(self, name, category, buying_price, selling_price, description):
        #A dictionary to store user details
        product_info = {}

        product_info['name'] = name
        product_info['category'] = category
        product_info['buying_price'] = buying_price
        product_info['selling_price'] = selling_price
        product_info['description'] = description
        product_info['id'] = 1 + len(self.products_list)

        # if re.match("^[0-9_]*$", buying_price) and re.match("^[0-9_]*$", selling_price):     
        self.products_list.append(product_info)
        return True
        # return "Selling or Buying price fields must be integers" 

    def get_all_products(self):
        if len(self.products_list) == 0:
            return "The products list is empty"
        else:
            return self.products_list

    def get_product_by_id(self, product_id):
        #Loop through the self.product_list to check for the product with the provided id
        for product in self.products_list:
            if product['id'] == product_id:
                return product
        else:
            return "The product id provided does not exist"


        


class SalesDetails():
     pass
    # Sales record constructor
    # def __init__(self):
        # A list to store sales record
        # self.sales_list = []

    # def create_sales(self, product_id):

        # A dictionary to hold sales details
        # sales_info = {}
        # sales_info['name'] = name
        # sales_info['category'] = category
        # sales_info['selling_price'] = selling_price
        # sales_info['id'] = len(self.sales_list) + 1
        # self.sales_list.append(sales_info)
        # return True   
    #     for product in products:
    #         if product['id'] == product_id:
    #             sales_info['name'] = product['name']
    #             sales_info['category'] = product['category']
    #             sales_info['selling_price'] = product['selling_price']
    #             sales_info['product_id'] = product['id']
    #             sales_info['id'] = len(self.sales_list) + 1
    #             self.sales_list.append(sales_info)
    #             return True
    #     else:
    #         return "No Product with that Id in the store"

    # def get_all_sales(self):
    #     if len(self.sales_list) == 0:
    #         return "The sales list is empty"
    #     else:
    #         return self.sales_list

    # def get_sale_by_id(self, sales_id):
    #     for sale in self.sales_list:
    #         if sale['id'] == sales_id:
    #             return sale
    #     else:
    #         return "No sale with that id is exists"
