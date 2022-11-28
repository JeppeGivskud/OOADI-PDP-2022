"""
A Proxy Concept Example
https://sbcode.net/python/proxy/#proxyproxy_conceptpy
"""
from abc import ABCMeta, abstractmethod

from Tools.scripts.treesync import raw_input


class IComponent(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject"
    @staticmethod
    @abstractmethod
    def method(self):
        """method to be implemented"""

class Component(IComponent):
    def method(self):
        print("the method has been called")

class ProxyComponent(IComponent):

    def __init__(self):
        self.component = Component()
        self.main()

    def method(self):
        self.component.method()

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

component2 = ProxyComponent()
#component2.method()