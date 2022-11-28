import pickle
import socket
import ListOfUsers

# No s.close is needed
class Client():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 40000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        self.recieve_text()

        self.ListOfUsers=ListOfUsers

    def connect(self):
        self.socket.connect((self.HOST, self.PORT))

    def send_text(self, message):
        self.socket.sendall(message.encode())
        self.recieve_text()

    def request_object(self, message):
        self.socket.sendall(message.encode())
        self.recieve_object()

    def recieve_text(self):
        data = self.socket.recv(1024)
        print('Ecco', repr(data))
        if data.decode() == 'Bye':
            print("Closing connection")
    def recieve_object(self):
        data = self.socket.recv(4096)
        #print('Ecco', repr(data))
        data_variable = pickle.loads(data)
        print(data_variable)
        self.ListOfUsers=data_variable
        #if data.decode() == 'Bye':
        #    print("Closing connection")

    def disconnect(self):
        self.send_text("Bye")


if __name__=="__main__":
    C = Client()
    message = input("What would you like? ")

    C.request_object(message)
    C.disconnect()
