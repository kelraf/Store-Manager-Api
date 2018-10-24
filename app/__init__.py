from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config

from .api.v1.models.products import ProductsDetails
from .api.v1.views import Products, SingleProduct, Sales, SingleSaleOrder, UserRegistration, LoginUser
products = ProductsDetails()
product_list = products.products_list

application_bp = Blueprint("application_bp", __name__, url_prefix="/api/v1")
api = Api(application_bp)

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config["development"])
    app.register_blueprint(application_bp)

    api.add_resource(Products, "/products")
    api.add_resource(SingleProduct, "/products/<int:id>")
    api.add_resource(Sales, "/sales")
    api.add_resource(SingleSaleOrder, "/sales/<int:id>")

    api.add_resource(UserRegistration, "/user")
    api.add_resource(LoginUser, "/login")
    return app