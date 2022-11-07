import socket

"""
HOST = '127.0.0.1'
PORT = 50000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        message = input("Enter message to send\n")
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received', repr(data))
        if (data.decode() == 'Bye'):
            print("Closing connection")
            break"""


# No s.close is needed
class Client():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.HOST, self.PORT))

    def send(self, message):
        self.socket.sendall(message.encode())
        self.recieve()

    def recieve(self):
        data = self.socket.recv(1024)
        print('Received', repr(data))
        if data.decode() == 'Bye':
            print("Closing connection")
    def disconnect(self):
        self.send("Bye")


C = Client()
C.connect()
C.send("Cheese")
C.send("Ball")
C.send("Fish")
C.send(input())
C.disconnect()
