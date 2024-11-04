class Cart:

    def __init__(self) -> None:
        self.orderItems = []

    def add_item(self, item):
        self.orderItems.append(item)

    def empty_card(self):
        self.orderItems = []

    