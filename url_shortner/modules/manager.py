from modules.urls import Urls
import string
import random

class UrlManager:

    def __init__(self) -> None:
        self.urls = {}

    def encode_url(self, url):
        url_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        Url =  Urls(url, url_id)

        self.urls[url_id] = Url
        return Url.encoded_url

    def access_url(self, url):

        urlc = self.urls[url.split('/')[1]]
        urlc.increment_click_count()

        return urlc.url






