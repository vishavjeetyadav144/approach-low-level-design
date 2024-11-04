class Order:

    def __init__(self, cart) -> None:
        
        self.cart = cart
        self.amount = self.place_order()
        self.status = "pending"

    def place_order(self):

        amount = 0 

        for item in self.cart.orderItems:

            if item.product.stock < item.quantity:
                print(f'{item.product.name} is not available , pls reduce quantity')
                break
                
            amount = amount + item.product.price * item.quantity
            item.product.update_stock(item.quantity)
        
        return amount

    def confirm_order(self):

        self.status = "confirmed"



            
