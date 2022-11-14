from Orders import *
import random

import pickle


class User():
    def __init__(self, name, e_mail):
        self.user_id = "cheese"
        self.GenerateID()
        self.name = name
        self.e_mail = e_mail

    def GenerateID(self):
        self.user_id = random.randint(0, 999999)


class SupportStaff(User):
    def __init__(self, user_name, user_password, name, e_mail):
        super().__init__(name, e_mail)
        self.user_password = user_password
        self.user_name = user_name

    def change_user_info(self, User):
        print(User)
        User.user_password = 333


class CostumerWithProfile(User):
    def __init__(self, user_name, user_password, phone_number, name, e_mail):
        super().__init__(name, e_mail)
        self.user_password = user_password
        self.user_name = user_name
        self.phone_number = phone_number
        self.Orderlist = []

    def retrieve_orderlist(self, Orderlist):
        self.Orderlist.append(Orderlist)


class CustomerWithoutProfile(User):
    def __init__(self, phone_number, name, e_mail):
        super().__init__(name, e_mail)
        self.phone_number = phone_number
        self.Order = Order

    def retrieve_orderlist(self, Order):
        self.Order = Order


class TivoliManagement(User):
    def __init__(self, user_name, user_password, name, e_mail):
        super().__init__(name, e_mail)
        self.user_password = user_password
        self.user_name = user_name

    def create_event(self):
        pass

    def change_event(self):
        pass

    def delete_event(self):
        pass

    def release_tickets(self):
        pass

    def view_tickets(self):
        pass


Costumer1 = CostumerWithProfile("username", "password", "62709977", "Dave", "Dave@gmail.com")
Costumer2 = CostumerWithProfile("username2", "password2", "62709957", "Jane", "Jane@gmail.com")

filename = "TwoTestCostumers.txt"  # File to save the pickled objects
with open(filename, 'wb') as pickle_file:  # Context manager to pickle the objects
    pickle.dump(Costumer1, pickle_file)  # Pickle my dog into file
    pickle.dump(Costumer2, pickle_file)  # Pickle your dog into file

filename = "TwoTestCostumers.txt"
with open(filename, "rb") as pickle_file:       # Open the file to read from
    my_dog = pickle.load(pickle_file)             # Load first object
    your_dog = pickle.load(pickle_file)

print(my_dog)
print(your_dog.name)