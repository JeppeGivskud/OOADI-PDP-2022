from OneDayTicket import*
from Ticket import*

class SoldTicket:

    def __init__(self,owner_id):
        self.owner_id = owner_id
        self.sold_ticket=self.create_ticket()

    def collect_ticket(self):
        return Ticket()
    def create_ticket(self):
        return Ticket()

    def set_owner_id(self, user_id):
        self.owner_id = user_id
