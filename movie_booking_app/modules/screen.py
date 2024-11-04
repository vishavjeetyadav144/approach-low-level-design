class Screen:
    
    def __init__(self, id, movie, occupancy) -> None:
        self.id = id
        self.movie = movie
        self.occupancy = occupancy
        self.tickets = {}

    def confirm_seats(self, ticket) -> None:
        self.occupancy = self.occupancy - ticket.seats 
        ticket.confirm_ticket(self.movie.price)
        self.tickets[ticket] = ticket

        

        
