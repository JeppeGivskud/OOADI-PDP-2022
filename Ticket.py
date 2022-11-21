import string
import random

class Ticket:

    ticket_id = "ticket id"
    ticket_used = False
    ticket_sold = False

    def __init__(self):
        self.generate_random_ticket_id()

    def generate_random_ticket_id(self):
        letters = string.ascii_lowercase  #disse to strimler af kode laver et tilfældig string i lower case
        self.ticket_id = ''.join(random.choice(letters) for i in range(10))

    def use_ticket(self):
        self.ticket_used = True
