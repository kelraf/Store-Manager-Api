from flask_restful import Resource
from flask import jsonify, request, make_response

from .models.products import ProductsDetails, SalesDetails
from .models.users import UserDetails

product = ProductsDetails()
sales = SalesDetails()

user = UserDetails()

""" Products Endpoints """

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


""" Sales Endpoints """

class Sales(Resource):

    def post(self):        

        sales_info = request.get_json()
        name = sales_info['name']
        category = sales_info['category']
        selling_price = sales_info['selling_price']
        response = sales.create_sales(name, category, selling_price)
        if response == True:
            return make_response(jsonify({"Status" : "Created", "Message" : "Sale Created Successfully", "Sales" : sales.sales_list}), 201)
        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : response})) 


    def get(self):
       response = sales.get_all_sales()
       return make_response(jsonify({"Status" : "Ok", "Message" : response, "Sales" : sales.sales_list}), 200)

class SingleSaleOrder(Resource):

    def get(self, id):
        response = sales.get_sale_by_id(id)
        return make_response(jsonify({"Status" : "Ok", "Sale" : response}), 200)



""" Users Endpoints """

class UserDetail(Resource):
    def post(self):
        user_info = request.get_json()
        
        username = user_info['username']
        email = user_info['email']
        password = user_info['password']
        confirm_password = user_info['confirm_password']

        response1 = user.register(username, email, password, confirm_password)
        if response1 == True:
            return make_response(jsonify({"Status" : "Created", "Message" : "User created successfully", "User" : user.user_list}), 201)

        else:
            return make_response(jsonify({"Status" : "Ok", "Message" : "User Not Created", "Reason" : response1}), 401)

    def get(self):
        pass