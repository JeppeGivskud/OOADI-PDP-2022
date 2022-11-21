from OneDayTicket import*


class SoldTicket:

    def __init__(self):
        self.owner_id = owner_id
        self.sold_ticket = sold_ticket

    def collect_ticket(self, ticket):
        self.sold_ticket = ticket

    def set_owner_id(self, user_id):
        self.owner_id = user_id
