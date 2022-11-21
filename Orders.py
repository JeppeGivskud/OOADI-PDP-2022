import pickle
from OneDayTicket import*
class Orders:
    def __init__(self):
        self.order_id = self.generate_random_order_id()
        self.tickets = []

    def generate_random_order_id(self):
        letters2 = string.ascii_lowercase
        return ''.join(random.choice(letters2) for i in range(10))
    def get_order_id(self):
        return self.order_id

    def collect_tickets(self, sold_ticket):
        self.tickets.append(sold_ticket)


if __name__=="__main__":
    Ticket1 = OneDayTicket("21/09")
    Ticket2 = OneDayTicket("29/09")
    Order1 = Orders()
    Order1.collect_tickets(Ticket1)
    Order1.collect_tickets(Ticket2)

    print(Order1.order_id)
    print(Order1.tickets[0].ticket_id)
    print(Order1.tickets[1].ticket_id)
    #Eksempel på at lave to tickets og en order som indeholder de tickets
    filename = "OrderExample.txt"  # File to save the pickled objects
    with open(filename, 'wb') as pickle_file:  # Context manager to pickle the objects
        pickle.dump(Ticket1, pickle_file)  # Pickle my dog into file
        pickle.dump(Ticket2, pickle_file)  # Pickle your dog into file
    with open(filename, "rb") as pickle_file:       # Open the file to read from
        my_dog = pickle.load(pickle_file)             # Load first object
        your_dog = pickle.load(pickle_file)
        print(my_dog.ticket_id)
        print(your_dog.ticket_id)

