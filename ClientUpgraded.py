import pickle
import socket
import sys

from User import CostumerWithProfile


# No s.close is needed
class Client():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.connect()


        self.User = CostumerWithProfile

    def connect(self):
        self.socket.connect((self.HOST, self.PORT))
        self.recieve_text()

    def send_text(self, message):
        self.socket.sendall(message.encode())
        self.recieve_text()

    def request_object(self, message):  # bruges ikke
        self.socket.sendall(message.encode())
        self.recieve_stuff()

    def recieve_text(self):  # bruges ikke
        data = self.socket.recv(1024)
        print('From server:', data.decode())
        if data.decode() == 'Bye':
            print("Closing connection")
    def login(self, username, password):
        message = f"{username};{password}"
        self.socket.sendall(message.encode())
        self.recieve_stuff()
    def recieve_stuff(self):
        data = self.socket.recv(4096)
        Isbye=False
        try:
            test = data.decode()
            print('From server:', test)
            if test=='Bye':
                Isbye=True
        except:
            User = pickle.loads(data)
            print(User)
            self.User = User
            print(self.User.order_list[0])
            #print(self.UserData.order_list[0].order_id)
            #print(self.UserData.order_list[0].ticket_list[0].sold_ticket.ticket_id)
            #print(self.UserData.order_list[0].ticket_list[0].sold_ticket.ticket_type)
            #print(self.UserData.order_list[0].ticket_list[0].date)
        if Isbye:
            print("Closing connection")
            sys.exit()

    def disconnect(self):
        self.send_text("Bye")
        print("Disconnecting")


if __name__ == "__main__":
    C = Client()
    C.connect()
    while True:
        e_mail = input("E-mail: ")
        password = input("Password: ")

        C.login(e_mail, password)
    C.disconnect()
