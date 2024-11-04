class Urls:

    def __init__(self, url, id):
        self.id = id
        self.url = url
        self.click_count = 0
        self.encoded_url = f'http://www.bitly/{id}'

    def increment_click_count(self):
        self.click_count += 1
