from faker import Faker

class User():
    def __init__(self, first_name,last_name, email, password, telephone, address, city, country, province, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.telephone = telephone
        self.address = address
        self.city = city
        self.country = country
        self.province = province
        self.postcode = postcode

    def user_fullname(self):
        return self.first_name + " " + self.last_name

    def user_email(self):
        return self.email

    def user_password(self):
        return self.password
