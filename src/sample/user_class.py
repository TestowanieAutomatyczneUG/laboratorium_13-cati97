class User:
    def __init__(self, user_id="", firstname="", lastname="", phone="", email=""):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email

    def get_firstname(self):
        return self.firstname
