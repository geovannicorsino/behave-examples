from faker import Faker


class UserLogin:
    def __init__(self):
        self.email = Faker().email()
