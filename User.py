from Order import *
import random

import pickle


class User():
    def __init__(self, name, e_mail):
        self.user_id = self.GenerateID()
        self.name = name
        self.e_mail = e_mail

    def GenerateID(self):
        random_id = random.randint(0, 999999)
        return random_id

class CostumerWithProfile(User):
    def __init__(self, user_name, user_password, phone_number, name, e_mail):
        super().__init__(name, e_mail)
        self.user_password = user_password
        self.user_name = user_name
        self.phone_number = phone_number
        self.order_list = []

    def get_user_password(self):
        return self.user_password

    def get_user_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def get_order_list(self):
        return self.order_list

    def set_user_password(self, new_password):
        self.user_password = new_password

    def set_user_name(self, new_name):
        self.name = new_name

    def set_phone_number(self, new_phone_nr):
        self.phone_number = new_phone_nr

    def add_order(self):
        new_order=Order()
        self.order_list.append(new_order)
        index = self.order_list.index(new_order)
        self.order_list[index].create_sold_ticket(self.user_id,"29/3")
        self.order_list[index].create_sold_ticket(self.user_id,"29/3")
        self.order_list[index].create_sold_ticket(self.user_id,"29/3")


if __name__ == "__main__":
    Costumer1 = CostumerWithProfile("username", "password", "62709977", "Dave", "Dave@gmail.com")
    Costumer1.add_order()
    Costumer1.add_order()
    Costumer1.add_order()
    print(Costumer1.order_list)
    print(Costumer1.order_list[0].order_id)
    print(Costumer1.order_list[0].ticket_list[0].sold_ticket.ticket_id)
    print(Costumer1.order_list[0].ticket_list[0].sold_ticket.ticket_type)
    print(Costumer1.order_list[0].ticket_list[0].date)


"""Example of two costumers
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
    your_dog2 = pickle.load(pickle_file)
"""

"""
class SupportStaff(User):
    def __init__(self, user_name, user_password, name, e_mail):
        super().__init__(name, e_mail)
        self.user_password = user_password
        self.user_name = user_name

    def change_user_info(self, User):
        print(User)
        User.user_password = 333

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
"""