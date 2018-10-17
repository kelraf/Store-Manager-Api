from flask_restful import Resource
from flask import jsonify, request, make_response

from .models import products, sales


class Products(Resource):

    def post(self):
        product_info = request.get_json()

        product_info['name']
        product_info['category']
        product_info['buying_price']
        product_info['selling_price']
        product_info['description']
        product_info['id'] = 1 + len(products)
        products.append(product_info)
        return make_response(jsonify({"Status" : "Created", "Message" : "Product Saved Successfully", "products" : products}), 201)


    def get(self):
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Products" : products}), 200)

class SingleProduct(Resource):
    def get(self, id):
        for product in products:
            if product['id'] == id:
                return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Product" : product}), 200)
        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : "No product with such id"}), 200)


class Sales(Resource):

    def post(self):
        sale_info = request.get_json()

        sale_info['name']
        sale_info['category']
        sale_info['selling_price']
        sale_info['description']
        sale_info['id'] = 1 + len(sales)

        sales.append(sale_info)
        return make_response(jsonify({"Status" : "Created", "Message" : "Sales created successfully", "Sales" : sales}), 201)


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