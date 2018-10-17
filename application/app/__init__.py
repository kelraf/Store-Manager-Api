from flask import Flask
from flask_restful import Api

from app.api.v1.views import Products, SingleProduct, Sales, SingleSaleOrder

app = Flask(__name__)
api = Api(app)


api.add_resource(Products, "/products")
api.add_resource(SingleProduct, "/products/<int:id>")
api.add_resource(Sales, "/sales")
api.add_resource(SingleSaleOrder, "/sales/<int:id>")
