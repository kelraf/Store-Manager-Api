import unittest
from flask import json

from app import app



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
        self.app = app.test_client()


    def test_post_products(self):
        response = self.app.post("/products", data = json.dumps(self.info), content_type = "application/json")

        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        response1 = self.app.get("/products")

        self.assertEqual(response1.status_code, 200)

    def test_get_product_by_id(self):
        response2 = self.app.get("/products/1")

        self.assertEqual(response2.status_code, 200)

    def test_post_sales_order(self):
        response3 = self.app.post("/sales", data = json.dumps(self.sales_info), content_type = "application/json")

        self.assertEqual(response3.status_code, 201)

    def test_get_all_sales_orders(self):
        response4 = self.app.get("/sales")

        self.assertEqual(response4.status_code, 200)