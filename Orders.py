class Orders:
    def __init__(self, order_id):
        self.order_id = order_id
        self.tickets = []

    def get_order_id(self):
        return self.order_id

    def collect_tickets(self, sold_ticket):
        self.tickets.append(sold_ticket)