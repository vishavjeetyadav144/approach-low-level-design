from modules.publisher import Publisher
from modules.topic import Topic
from modules.subscriber import Subscriber
from modules.message import Messages

def main():

    subscriber1 = Subscriber(1)
    subscriber2 = Subscriber(2)

    topic = Topic("topic", [subscriber1, subscriber2])
    publisher = Publisher(topic)

    while True:
        msg = input("Enter message - ")
        message = Messages(msg)
        publisher.publish_message_to_topic(message)

if __name__ == "__main__":
    main()