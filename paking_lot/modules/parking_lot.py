
from modules.tickets import Ticket
from modules.parking_spot import ParkingSpot

class ParkingLot:

    def __init__(self, bikes, cars, trucks) -> None:

        self.bike_spots = []
        for i in range(bikes): 
            self.bike_spots.append(ParkingSpot("bike", 1, f'b{i}'))

        self.car_spots = []
        for i in range(cars):
            self.car_spots.append(ParkingSpot("car", 1, f'c{i}'))
        
        self.truck_spots = []
        for i in range(trucks):
            self.truck_spots.append(ParkingSpot("truck", 1, f't{i}'))

        self.tickets = []

    def park_vehicle(self, vehicle) -> str:

        ticket = None

        if vehicle.type == "bike":
            for lot in self.bike_spots:
                if lot.is_occupied == False:
                    ticket = Ticket(vehicle, lot)
                    break
        elif vehicle.type == "car":
            for lot in self.car_spots:
                if lot.is_occupied == False:
                    ticket = Ticket(vehicle, lot)
                    break

        elif vehicle.type == "truck":
            for lot in self.car_spots:
                if lot.is_occupied == False:
                    ticket = Ticket(vehicle, lot)
                    break

        if ticket is not None:
            self.tickets.append(ticket)

        return ticket

    def unpark_vehicle(self, ticket_id) -> bool:

        ticket = None
        for i in range(len(self.tickets)):

            if self.tickets[i].id == ticket_id:
                ticket = self.tickets[i].id
                break
        
        if ticket is not None:

            fair = ticket.calculate_fair_price()
            self.tickets = self.tickets[:i]+ self.tickets[i+1]
            return fair
        else:
            return None



        
        

        


    

        
    