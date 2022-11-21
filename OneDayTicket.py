from Ticket import *


class OneDayTicket(Ticket):

    number_uses = 1
    date = ""

    def __init__(self, date):
        super().__init__()
        self.date = date
        self.set_ticket_type_to_OneDay()


    def set_ticket_type_to_OneDay(self):
        self.ticket_id = "1D" + self.ticket_id

