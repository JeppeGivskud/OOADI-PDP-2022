import string
import random

class Ticket:

    ticket_id = "ticket id"
    ticket_used = False
    ticket_sold = False

    def __init__(self):
        print("init called")

    def generate_random_ticket_id(self):
        letters2 = string.ascii_lowercase
        self.ticket_id = ''.join(random.choice(letters2) for i in range(10))

    def use_ticket(self):
        self.ticket_used = True
