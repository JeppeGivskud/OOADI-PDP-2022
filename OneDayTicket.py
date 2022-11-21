from Ticket import *


class OneDayTicket(Ticket):

    number_uses = 1
    date = ""

    def __init__(self, date):
        super().__init__()
        self.date = date
        self.set_ticket_type_to_OneDay()


    def set_ticket_type_to_OneDay(self):
        letters2 = string.ascii_lowercase
        self.ticket_id = "1D" + self.ticket_id


if __name__ == "__main__":

    ohi = OneDayTicket("12/13")
    print(ohi.ticket_id)
