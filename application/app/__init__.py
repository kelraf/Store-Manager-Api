from flask import Flask
from flask_restful import Api

from app.api.v1.views import Products, SingleProduct

app = Flask(__name__)
api = Api(app)


api.add_resource(Products, "/products")
api.add_resource(SingleProduct, "/products/<int:id>")

