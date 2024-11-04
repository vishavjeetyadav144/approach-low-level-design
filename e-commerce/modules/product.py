class Product:

    def __init__(self, name, category, stock, price) -> None:

        self.name = name
        self.category = category
        self.stock = stock 
        self.price = price

    def get_details(self , index):
        print(f'Name - {self.name} category - {self.category} price - {self.price} , Press -{index} to add to cart')

    
    def refill_stock(self, quantity):
        self.stock += quantity

    def update_stock(self, quantity):
        self.stock -= quantity