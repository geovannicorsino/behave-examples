from faker import Faker


class User:
    def __init__(self):
        self.email = Faker().email()
        self.name = Faker().name()
        self.password = Faker().password()
