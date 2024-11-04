class Subscriber:
    
    def __init__(self, id) -> None:
        self.id = id

    def receive_message(self, message):
        print(f'received message content - {message.content} id - {self.id}')