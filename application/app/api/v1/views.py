from flask_restful import Resource
from flask import jsonify, request, make_response

from .models import products


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
