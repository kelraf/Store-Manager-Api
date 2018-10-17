import unittest



class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()


    def test_get_all_products(self):
        response = self.app.get('/products')

        self.assertEqual(response.status_code, 200)