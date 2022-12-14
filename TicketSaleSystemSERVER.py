import socket
import threading
from typing import Type

from ListOfUsers import *


class ClientThread(threading.Thread):
    ListOfUsers: Type[ListOfUsers]

    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.database = ListOfUsers()  # initiere en database som kan tilføje brugerobjekter
        self.load_users()

        print("Database loaded:")
        repr(self.database)

        self.csocket = client_socket
        # self.database.Example()
        # ListOfUsers.Example()  # Laver 4 brugere som kan bruges som eksempler

    def load_users(self):
        filename = "AllUsers.txt"
        with open(filename, "rb") as pickle_file:  # Open the file to read from
            self.database = pickle.load(pickle_file)  # Load first object

    def run(self):
        with self.csocket:
            self.csocket.sendall(b'Connected to server')  # send string to client
            while True:
                data = self.csocket.recv(1024)  # data received from client

                datastring = data.decode()
                datastring = datastring.split(";")
                if (datastring[0] == 'Bye'):
                    print("Closing connection")
                    self.csocket.sendall(b'Bye')  # send back echo string to client
                    break
                else:
                    print(datastring)
                    self.login(datastring)
                # self.check_password(data)
                # self.csocket.sendall(data)  # send back echo string to client


    def login(self, datastring):
        if len(datastring)==2:
            e_mail=datastring[0]
            password=datastring[1]
            for user in self.database.customers:
                if user.e_mail == e_mail:
                    print("correct email")
                    if user.user_password == password:
                        print("correct password")
                        return self.send_pickled_object(user)
                    return self.send_text("Wrong password")
                return self.send_text("Wrong email")
            return self.send_text("No user exists with that name")

    def send_text(self,message):
        self.csocket.sendall(message.encode())  # send back echo string to client
        print(f'"{message}" sent to client')

    def send_pickled_object(self, object):
        data_string = pickle.dumps(object)
        self.csocket.sendall(data_string)  # send back echo string to client
        print(f"Object sent to client")


if __name__ == "__main__":
    host = 'localhost'
    port = 50000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        range = 0
        while range < 100:
            client_socket, client_address = s.accept()  # connect to a new client
            client_thread = ClientThread(client_socket)  # start a new thread
            client_thread.start()
            range = range + 1
