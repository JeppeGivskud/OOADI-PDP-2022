import socket


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
        print('Ecco', repr(data))
        if data.decode() == 'Bye':
            print("Closing connection")

    def disconnect(self):
        self.send("Bye")


"""
C = Client()
C.connect()
C.send("Cheese")
C.send("Ball")
C.send("Fish")
C.send(input())
C.disconnect()
"""
