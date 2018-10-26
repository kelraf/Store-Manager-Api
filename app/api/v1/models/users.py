import re

class UserDetails():
    def __init__(self):
        #A list to store the attendant Details
        self.user_list = []

    #Validator
    def validate_data(self, username, email, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", username)\
        or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 6:
            return "Username should be atleast six characters long"
        elif len(password) < 6:
            return "Password should be atleast six characters long"
        elif password != confirm_password:
            return "Passwords should match"
        else:
            return True

    #A method to register attendant
    def register(self, username, email, password, confirm_password):
        #A dict to store attendant info
        user_infor = {}

        if len(self.user_list) > 0:
            #loop through the list to check if the attendant with the provided email or username exists
            for user in self.user_list:
                if user['username'] == username or user['email'] == email:
                    return "Username or email already exists"
            else:
                #attendant does not exist validate the data provided
                validate = self.validate_data(username, email, password, confirm_password)
                if validate == True:

                    #if data validation passes register the user
                    user_infor['username'] = username
                    user_infor['email'] = email
                    user_infor['password'] = password
                    user_infor['confirm_password'] = confirm_password
                    user_infor['id'] = len(self.user_list) + 1
                    user_infor['Admin'] = False
                    self.user_list.append(user_infor)
                    return True
                else:
                    #if data is invalid return the message indicating the problem
                    return validate

        #The userlist is empty validate the data
        else:
            validate = self.validate_data(username, email, password, confirm_password)
            if validate == True:
                #The data is valid 
                #Register the user
                user_infor['username'] = username
                user_infor['email'] = email
                user_infor['password'] = password
                user_infor['confirm_password'] = confirm_password
                user_infor['id'] = len(self.user_list) + 1
                user_infor['Admin'] = True
                self.user_list.append(user_infor)
                return True
            #if data is invalid return the message indicating the problem
            else:
                return validate

    #A method to get all users
    def get_all_user(self):
        user = self.user_list
        return user

    #A method to login an attendant
    def provide_user_list(self):

        user = self.user_list
        return user