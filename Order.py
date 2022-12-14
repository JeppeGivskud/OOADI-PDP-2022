import pickle
from OneDayTicket import *
from SoldTicket import *
from User import *


class Order:
    def __init__(self):
        self.order_id = self.generate_random_order_id()
        self.ticket_list = []

    def __repr__(self):
        counter=1
        print(f'Order: "{self.order_id}" has {len(self.ticket_list)} Tickets')
        representation = f'Order: "{self.order_id}" has {len(self.ticket_list)} Tickets for "{self.ticket_list[0].date}" \n'
        for sold_ticket in self.ticket_list:
            representation+=f'Ticket {counter}: "{sold_ticket.sold_ticket.ticket_id}"' \
                            f'is a "{sold_ticket.sold_ticket.ticket_type}"\n'
            counter+=1
        return representation

    def generate_random_order_id(self):
        letters2 = string.ascii_lowercase
        return ''.join(random.choice(letters2) for i in range(10))

    def get_order_id(self):
        return self.order_id

    def collect_sold_tickets(self, sold_ticket):
        self.ticket_list.append(sold_ticket)

    def create_sold_ticket(self, owner_name, date):
        self.ticket_list.append(SoldTicket(owner_name, date))
        self.ticket_list.append(SoldTicket(owner_name, date))
        self.ticket_list.append(SoldTicket(owner_name, date))


if __name__ == "__main__":
    MyUser = User("Yvonne Nielsen", "iamyvonne@nielsen.dk")
    MyUser.GenerateID()

    Ticket1 = OneDayTicket("21/09")
    Ticket2 = OneDayTicket("29/09")
    SoldTicket1 = SoldTicket()
    SoldTicket1.collect_ticket(Ticket1)
    SoldTicket1.set_owner_id(MyUser.user_id)

    SoldTicket2 = SoldTicket()
    SoldTicket2.collect_ticket(Ticket2)
    SoldTicket2.set_owner_id(MyUser.user_id)

    Order1 = Order()
    Order1.collect_sold_tickets(SoldTicket1)
    Order1.collect_sold_tickets(SoldTicket2)

    print(SoldTicket1.sold_ticket)
    print(SoldTicket1.owner_id)
    print(SoldTicket2.sold_ticket)
    print(SoldTicket2.owner_id)
    print(Order1.order_id)
    print(Order1.ticket_list[0].ticket_id)
    print(Order1.ticket_list[1].ticket_id)
    # Eksempel p?? at lave to tickets og en order som indeholder de tickets
    filename = "OrderExample.txt"  # File to save the pickled objects
    with open(filename, 'wb') as pickle_file:  # Context manager to pickle the objects
        pickle.dump(Order1, pickle_file)  # Pickle my dog into file
