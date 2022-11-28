import socket
import threading
from ListOfUsers import *


class ClientThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.Database = ListOfUsers  # initiere en database som kan tilføje brugerobjekter
        ListOfUsers.Example()  # Laver 4 brugere som kan bruges som eksempler

    def run(self):
        with self.csocket:
            while True:
                data = self.csocket.recv(1024)  # data received from client
                self.check_password(data)
                self.csocket.sendall(data)  # send back echo string to client
                if (data.decode() == 'Bye'):
                    print("Closing connection")
                    break

    def check_password(self, username):
        if username == b'yvonne':
            self.csocket.sendall(b'password')


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
