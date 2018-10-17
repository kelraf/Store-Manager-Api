from flask import Flask
from flask_restful import Api

from app.api.v1.views import Products

app = Flask(__name__)
api = Api(app)


api.add_resource(Products, "/products")

