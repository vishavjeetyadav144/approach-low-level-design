from enums.tickets import TicketStatusEnum

class Ticket:

    def __init__(self, id, screen, seats) -> None:
        self.id = id
        self.screen = screen
        self.amount = None
        self.seats = seats
        self.status = TicketStatusEnum.PENDING

    def confirm_ticket(self, price) -> None:
        self.amount = price* len(self.seats)
        self.status = TicketStatusEnum.CONFIRMED

    def cancel_ticket(self) -> None:
        self.status = TicketStatusEnum.CANCELED
        