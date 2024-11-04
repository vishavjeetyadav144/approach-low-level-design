
class ParkingSpot:

    def __init__(self, type, lot, id) -> None:
        self.type =  type
        self.is_occupied = False
        self.lot = lot
        self.id = id

    def park_vehicle(self) -> None:
        self.is_occupied = True

    def unpark_vehicle(self) -> None:
        self.is_occupied = False

