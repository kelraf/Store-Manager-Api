import unittest
from flask import json

from app import create_app



class TestApi(unittest.TestCase):

    info = {
        "name" : "name",
        "category" : "category",
        "buying_price" : "buying_price",
        "selling_price" : "selling_price",
        "description" : "description",
        "id" : "id"
    }

    sales_info = {
        "name" : "name",
        "category" : "category",
        "selling_price" : "selling_price",
        "description" : "description",
        "id" : "id"
    }
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client


    def test_post_products(self):
        response = self.client().post("/api/v1/products", data = json.dumps(self.info), content_type = "application/json")

        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        response1 = self.client().get("/api/v1/products")

        self.assertEqual(response1.status_code, 200)

    def test_get_product_by_id(self):
        response2 = self.client().get("/api/v1/products/1")

        self.assertEqual(response2.status_code, 200)

    def test_post_sales_order(self):
        response3 = self.client().post("/api/v1/sales", data = json.dumps(self.sales_info), content_type = "application/json")

        self.assertEqual(response3.status_code, 201)

    def test_get_all_sales_orders(self):
        response4 = self.client().get("/api/v1/sales")

        self.assertEqual(response4.status_code, 200)

    def test_get_a_specific_order(self):
        response5 = self.client().get("/api/v1/sales/1")

        self.assertEqual(response5.status_code, 200)