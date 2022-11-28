"""
A Proxy Concept Example
https://sbcode.net/python/proxy/#proxyproxy_conceptpy
"""

from Orders import *
import random

import pickle

from abc import ABCMeta, abstractmethod

from Tools.scripts.treesync import *


class IComponent(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject"
    @staticmethod
    @abstractmethod
    def method(self):
        """method to be implemented"""

class User(IComponent):

    def __init__(self, name, e_mail):
        self.user_id = self.GenerateID()
        self.name = name
        self.e_mail = e_mail

    def GenerateID(self):
        random_id = random.randint(0, 999999)
        return random_id


    def method(self):
        print("the method has been called")

    def GenerateID(self):
        random_id = random.randint(0, 999999)
        return random_id

class ProxyUser(IComponent):

    def __init__(self):
        #login
        self.user = User(self, self)
        self.main()

    def method(self):
        self.user.method()


    def login(self):
        user = input("Username: ")
        passw = input("Password: ")
        f = open("users.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split()
            if (user in us) and (passw in pw):
                return True
        print("du er ikke inde")
        return False

    def main(self):
        log = self.login()
        if log == True:
            print("du er inde")


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

    def set_orderlist(self, Orderlist):
        self.order_list = Orderlist

component2 = ProxyUser()
#component2.method()

