from modules.user import User
from modules.cart import Cart
from modules.product import Product
from modules.orderItem import OrderItem
from modules.order import Order

def get_list_of_product(products):    
    for index in range(len(products)):
        products[index].get_details(index)

def get_user_cart(cart):
    for item in cart.orderItems:
        print(f'{item.product.name} - {item.quantity}')

def place_order(cart):
    order = Order(cart)
    return order

def main():

    # mock data
    cart = Cart()
    user = User(1, cart)
    products = [ 
        Product("jeans", "apparel", 10, 499), 
        Product("bike", "toy", 5, 199), 
        Product("watch", "gadget", 2, 1999)
    ]

    while True:

        print("get list of product - 1")
        print("get check cart - 2")
        print("get place order - 3")
        print("to exit - -1")

        try:
            i = int(input("Enter here - "))
            if i  == -1:
                break

            if i == 1:
                get_list_of_product(products)
                while True:
                    try:
                        pid = int(input("want to add product to cart press number - \n for main menu - -1 \n Enter here - "))
                        if pid  == -1:
                            break
                        quantity = int(input("quantity - "))
                        if pid < len(products):

                            if quantity <= products[pid].stock:
                                item = OrderItem(products[pid], quantity)  
                                user.cart.add_item(item)
                            else:
                                print("available quantity is less") 
                        else:
                            print("enter valid input")
                    except ValueError:
                        print("enter valid input")
            elif i == 2:
                get_user_cart(user.cart)
            elif i == 3: 
                order = place_order(user.cart)

                print(f'Final order amount is - {order.amount}')
                i = input("To confirm press - y \n press here - ")

                if i == "y":
                    order.confirm_order()
                    user.add_order(order)
                else:
                    break
            else:
                print("Enter Valid input")
        except ValueError:
            print(f'')
    
if __name__ == "__main__":
    main()