
class UrlManager:
    def __init__(self, root_url):
        self.urls = set()
        self.urls.add(root_url)

    def add_new_url(self, new_url):
        if new_url is not None:
            self.urls.add(new_url)

    def get_new_url(self):
        return self.urls.pop()

