import unittest
from app.api.v1.models.users import UserDetails

class Test_user(unittest.TestCase):

    def setUp(self):
        self.users = UserDetails()

    def test_user_registration_successful(self):

        response = self.users.register("kelraf", "rafwambugu@gmail.com", "kelraf", "kelraf")
        self.assertTrue(response)

    def test_registation_with_invalid_details(self):

        response1 = self.users.register("kelrf", "rafwambugu@gmail.com", "kelraf", "kelraf")

        self.assertEqual(response1, "Username should be atleast six characters long")

    def test_validation_with_valid_datails(self):
        response2 = self.users.validate_data("kelraf", "rafwambugu@gmail.com", "kelraf", "kelraf")

        self.assertTrue(response2)

    def test_validate_with_username_with_less_than_six_characters(self):
        response3 = self.users.validate_data("kelrf", "rafwambugu@gmail.com", "kelraf", "kelraf")

        self.assertEqual(response3, "Username should be atleast six characters long")

    def test_validate_with_invalid_username(self):
         response4 = self.users.validate_data("kelr^f", "rafwambugu@gmail.com", "kelraf", "kelraf")

         self.assertEqual(response4, "Username or email can only contain alphanumeric characters")

    def test_validate_with_invalid_email(self):
        response5 = self.users.validate_data("kelraf", "rafwambugugmail.com", "kelraf", "kelraf")

        self.assertEqual(response5, "Username or email can only contain alphanumeric characters")

    def test_validate_with_unmatching_passwords(self):
        response6 = self.users.validate_data("kelraf", "rafwambugu@gmail.com", "kelr2f", "kelraf")

        self.assertEqual(response6, "Passwords should match")

    def test_validate_with_password_less_than_six_characters(self):
        response7 = self.users.validate_data("kelraf", "rafwambugu@gmail.com", "kelra", "kelra")

        self.assertEqual(response7, "Password should be atleast six characters long")

