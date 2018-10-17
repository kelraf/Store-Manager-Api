import unittest
from flask import json

from app import app



class TestApi(unittest.TestCase):

    info = {
        "name" : "name",
        "category" : "category",
        "buying_price" : "buying_price",
        "selling_price" : "selling_price",
        "description" : "description"
    }
    
    def setUp(self):
        self.app = app.test_client()


    def test_post_products(self):
        response = self.app.post("/products", data = json.dumps(self.info), content_type = "application/json")

        self.assertEqual(response.status_code, 201)