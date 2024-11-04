class User:

    def __init__(self, id, cart) -> None:
        self.id = id
        self.orders = []
        self.cart = cart

    def add_order(self, order):
        self.orders.append(order)
        self.cart.empty_card()