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

    #Test registration with valid details
    attendant_info_correct = {
        "username" : "kelraf",
        "email" : "email@gmail.com",
        "password" : "password",
        "confirm_password" : "password"
    }

    def test_post_attendant_registration_infor_success(self):
        response6 = self.client().post("/api/v1/attendant", data = json.dumps(self.attendant_info_correct), content_type = "application/json")

        self.assertEqual(response6.status_code, 201)

    #Test registration with invalid details 
    attendant_info_wrong = {
        "username" : "kelra",
        "email" : "email@gmail.com",
        "password" : "password",
        "confirm_password" : "password"
    }


    def test_post_attendant_registration_infor_errors(self):
        response7 = self.client().post("/api/v1/attendant", data = json.dumps(self.attendant_info_wrong), content_type = "application/json")

        self.assertEqual(response7.status_code, 409)

    #Test getting all the attendants
    attendant_info_correct_one = {
        "username" : "kelrif",
        "email" : "emailraf@gmail.com",
        "password" : "password",
        "confirm_password" : "password"
    }

    def test_get_all_attendants_list_not_empty(self):

        response8 = self.client().post("/api/v1/attendant", data = json.dumps(self.attendant_info_correct_one), content_type = "application/json")
        response9 = self.client().get("/api/v1/attendant")
        
        self.assertEqual(response9.status_code, 200)


    #Data to register a user so as to login
    attendant_info_correct_reg = {
        "username" : "kimjam",
        "email" : "emailrafw@gmail.com",
        "password" : "kim1234",
        "confirm_password" : "kim1234"
    }


    #Data to login
    att_login = {
        "username" : "kimjam",
        "password" : "kim1234"
    }
    
    def test_login_attendant_successfull(self):
        response10 = self.client().post("api/v1/attendant", data = json.dumps(self.attendant_info_correct_reg), content_type = "application/json")
        response11 = self.client().post("/api/v1/login", data = json.dumps(self.att_login), content_type = "application/json")

        self.assertEqual(response11.status_code, 202)


    #Login unregistered attendant
    unreg_att = {
        "username" : "rafking",
        "password" : "kim1234"
    }
    
    def test_login_unregistered_attendant(self):
        response12 = self.client().post("/api/v1/login", data = json.dumps(self.unreg_att), content_type = "application/json")

        self.assertEqual(response12.status_code, 401)


