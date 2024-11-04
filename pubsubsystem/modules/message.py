from datetime import datetime

class Messages:

    def __init__(self, content) -> None:
        self.content = content
        self.time = datetime.now()