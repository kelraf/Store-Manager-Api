import re

class UserDetails():
    def __init__(self):
        #A list to store the Admin Details
        self.user_list = []

    def validate_data(self, username, email, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", username):
            return "Your username should only contain alphanumeric charackers"
        elif len(username.strip()) < 6:
            return "Your username should be atleast six characters long"
        elif len(password) < 6:
            return "Your password should be atleast six characters long"
        elif password != confirm_password:
            return "Your passwords should match"
        else:
            return True

    def register(self, username, email, password, confirm_password):
        #A dict to store user info
        user_infor = {}

        validate = self.validate_data(username, email, password, confirm_password)
        if validate == True:
            user_infor['username'] = username
            user_infor['email'] = email
            user_infor['password'] = password
            user_infor['confirm_password'] = confirm_password
            user_infor['id'] = len(self.user_list) + 1
            self.user_list.append(user_infor)
            return True
        else:
            return validate