import threading

class Topic:

    def __init__(self, name, subscribers) -> None:
        self.name = name
        self.subscribers = subscribers

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def publish_message(self, message):
        for subscriber in self.subscribers:
            threading.Thread(subscriber.receive_message(message)).start()
        
    