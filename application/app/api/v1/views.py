from flask_restful import Resource
from flask import jsonify, request, make_response

from .models.products import products, sales, ProductsDetails


product = ProductsDetails()


class Products(Resource):

    def post(self):
        product_info = request.get_json()

        name = product_info['name']
        category = product_info['category']
        buying_price = product_info['buying_price']
        selling_price = product_info['selling_price']
        description = product_info['description']

        #call the create function 
        response = product.create_product(name, category, buying_price, selling_price, description)
        if response == True:
            return make_response(jsonify({"Status" : "Created", "Message" : "Product Saved Successfully", "Products" : product.products_list}), 201)
        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : response}))

    def get(self):
        #call get all method from Products details class
        response = product.get_all_products()
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Products" : response}), 200)

class SingleProduct(Resource):
    def get(self, id):
        #call get a product by id method from Products details class
        response = product.get_product_by_id(id)
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Product" : response}), 200)

class Sales(Resource):

    def post(self):        

        product_id = request.get_json()
        product_id['product_id']
        for product_d in products:
            if product_d['id'] == product_id['product_id']:
                sales_info = {}
                sales_info['name'] = product_d['name']
                sales_info['category'] = product_d['category']
                sales_info['selling_price'] = product_d['selling_price']
                sales_info['product_id'] = product_d['id']
                sales_info['id'] = 1 + len(sales)
                sales.append(sales_info)
                products.remove(product_d)
                return make_response(jsonify({"Status" : "Created", "Message" : "Sales created successfully", "Sales" : sales}), 201)
        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : "No product with that id"}))

    def get(self):
        if len(sales) == 0:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Sales record is empty", "Sales" : sales}), 200)
        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Sales" : sales}), 200)


class SingleSaleOrder(Resource):

    def get(self, id):
        for sale in sales:
            if sale['id'] == id:
                return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Sale" : sale}), 200)

        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : "No order with that id"}), 200)