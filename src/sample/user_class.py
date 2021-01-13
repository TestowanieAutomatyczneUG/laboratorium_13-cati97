import re

class User:
    def __init__(self, user_id="", firstname="", lastname="", phone="", email=""):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def create_fullname(self, firstname, lastname):
        return f"{firstname} {lastname}"

    def check_email_is_correct(self):
        if not re.match(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$", self.email):
            return "Incorrect"
        else:
            return "Correct"

    def check_phone_is_int(self):
        if type(self.phone) is int:
            return True
        else:
            return False

