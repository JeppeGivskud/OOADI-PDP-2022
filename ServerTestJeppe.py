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
        #self.database.Example()
        #ListOfUsers.Example()  # Laver 4 brugere som kan bruges som eksempler
    def load_users(self):
        filename = "AllUsers.txt"
        with open(filename, "rb") as pickle_file:  # Open the file to read from
            self.database = pickle.load(pickle_file)  # Load first object

    def run(self):
        with self.csocket:
            self.csocket.sendall(b'Connected to server')  # send string to client
            while True:
                data = self.csocket.recv(1024)  # data received from client

                datastring=data.decode()
                datastring=datastring.split(";")
                print(datastring)
                self.login(datastring[0],datastring[1])
                #self.check_password(data)
                #self.csocket.sendall(data)  # send back echo string to client
                if (data.decode() == 'Bye'):
                    print("Closing connection")
                    break

    def login(self,username,password):
        for user in self.database.customers:
            if user.name == username:
                print("correct username")
                if user.user_password == password:
                    print("correct password")
                    self.send_pickled_object(user)
    def send_pickled_object(self,object):
        data_string = pickle.dumps(object)
        self.csocket.sendall(data_string)  # send back echo string to client
        print(f"Object sent to Server")

if __name__ == "__main__":
    host = 'localhost'
    port = 40000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        range = 0
        while range < 1:
            client_socket, client_address = s.accept()  # connect to a new client
            client_thread = ClientThread(client_socket)  # start a new thread
            client_thread.start()
            range = range + 1
