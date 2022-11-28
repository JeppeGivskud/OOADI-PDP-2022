import pickle
import socket
from User import CostumerWithProfile


# No s.close is needed
class Client():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        self.recieve_text()

        self.UserData = CostumerWithProfile

    def connect(self):
        self.socket.connect((self.HOST, self.PORT))

    def send_text(self, message):
        self.socket.sendall(message.encode())
        self.recieve_text()

    def request_object(self, message):  # bruges ikke
        self.socket.sendall(message.encode())
        self.recieve_stuff()

    def login(self, username, password):
        message = f"{username};{password}"
        self.socket.sendall(message.encode())
        self.recieve_stuff()

    def recieve_text(self):  # bruges ikke
        data = self.socket.recv(1024)
        print('From server:', data.decode())
        if data.decode() == 'Bye':
            print("Closing connection")

    def recieve_stuff(self):
        data = self.socket.recv(4096)
        try:
            test = data.decode()
            print('From server:', test)
            if test == 'Bye':
                print("Closing connection")
        except:
            data_variable = pickle.loads(data)
            print(data_variable)
            self.UserData = data_variable
            print(self.UserData.order_list)
            #print(self.UserData.order_list[0].order_id)
           # print(self.UserData.order_list[0].ticket_list[0].sold_ticket.ticket_id)
           # print(self.UserData.order_list[0].ticket_list[0].sold_ticket.ticket_type)
            #print(self.UserData.order_list[0].ticket_list[0].date)

    def disconnect(self):
        self.send_text("Bye")
        print("Disconnecting")


if __name__ == "__main__":
    C = Client()
    while True:
        username = input("Username: ")
        password = input("Password: ")

        C.login(username, password)
    C.disconnect()
