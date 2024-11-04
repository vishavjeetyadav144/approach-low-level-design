class Publisher:

    def __init__(self, topic) -> None:
        self.topic = topic

    def publish_message_to_topic(self, message):
        self.topic.publish_message(message)