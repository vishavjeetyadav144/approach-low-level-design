from modules.parking_lot import ParkingLot
from modules.vehicles import Vehicle
if __name__ == "__main__":

    parkinglot = ParkingLot(3,2,2)

    vehicle_map = {
        1: 'bike',
        2: 'car',
        3: 'truck'
    }

    while True:

        print(''' To park vehicle - 1 \n To unpark vehicle - 2 \n''')
        try:
            number = int(input('Enter here ------ '))
            if number == 1:
                print(''' To park bike type 1 \n to park car type 2 \n to park truck type 3 \n''')
                vehicle_type = int(input("enter here"))
                if vehicle_type >=1 and vehicle_type <= 3:
                    vehicle_number = input("Enter vehicle number here - ")  
                    ticket  = parkinglot.park_vehicle(Vehicle(vehicle_number, vehicle_map[vehicle_type]))

                    if ticket is not None:
                        print(f'your ticket number is -- {ticket.id}')
                    else:
                        print(f'Parking spot not available ')
                else:
                    print("please enter valid vehicle type")
            
            elif number == 2:
                ticket_number = int(input("enter your ticket number - "))
                fair = parkinglot.unpark_vehicle(ticket_number)
                if fair is not None:
                    print(f'your fair amount is -  {fair}')

                else:
                    print('pls enter valid ticket number ')
                 
        except ValueError:
            print("enter a valid input")
