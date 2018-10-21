import re

class AttendantDetails():
    def __init__(self):
        #A list to store the attendant Details
        self.attendant_list = []

    #Validator
    def validate_data(self, username, email, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", username):
            return "Username should only contain alphanumeric charackers"
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
        attendant_infor = {}

        if len(self.attendant_list) > 0:
            #loop through the list to check if the attendant with the provided email or username exists
            for user in self.attendant_list:
                if user['username'] == username or user['email'] == email:
                    return "Username or email already exists"
            else:
                #attendant does not exist validate the data provided
                validate = self.validate_data(username, email, password, confirm_password)
                if validate == True:

                    #if data validation passes register the user
                    attendant_infor['username'] = username
                    attendant_infor['email'] = email
                    attendant_infor['password'] = password
                    attendant_infor['confirm_password'] = confirm_password
                    attendant_infor['id'] = len(self.attendant_list) + 1
                    self.attendant_list.append(attendant_infor)
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
                attendant_infor['username'] = username
                attendant_infor['email'] = email
                attendant_infor['password'] = password
                attendant_infor['confirm_password'] = confirm_password
                attendant_infor['id'] = len(self.attendant_list) + 1
                self.attendant_list.append(attendant_infor)
                return True
            #if data is invalid return the message indicating the problem
            else:
                return validate

    #A method to get all users
    def get_all_attendants(self):
        attendants = self.attendant_list
        return attendants

    #A method to login an attendant
    def provide_attendants_list(self):

        attendants = self.attendant_list
        return attendants