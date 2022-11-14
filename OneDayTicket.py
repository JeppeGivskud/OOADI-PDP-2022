from Ticket import *


class OneDayTicket(Ticket):

    number_uses = 1
    date = ""

    def __init__(self, date):
        super().__init__()
        self.date = date

    def set_ticket_type_to_OneDay(self):
        letters2 = string.ascii_lowercase
        self.ticket_id = "1D" + ''.join(random.choice(letters2) for i in range(10))


if __name__ == "__main__":
    hi = Ticket()
    hi.generate_random_ticket_id()
    print(hi.ticket_id)

    ohi = OneDayTicket("12/13")
    ohi.set_ticket_type_to_OneDay()
    print(ohi.ticket_id)
