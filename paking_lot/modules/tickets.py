import datetime
import random
import string

class Ticket:

    def __init__(self, vehicle, spot) -> None:

        self.id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        self.vehicle = vehicle
        self.spot = spot
        self.entry_at = datetime.datetime.now()
        self.exit_at = None
        self.fair_amount = None
        spot.park_vehicle()

    def calculate_fair_price(self):
        exit_at = datetime.datetime.now()
        duration = exit_at - self.entry_at

        if duration.total_seconds < 3600:
            self.fair_amount = 50
        else:

            self.fair_amount = 100

        self.spot.unpark_vehicle()

        return self.fair_amount

