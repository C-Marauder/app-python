
class UrlManager:

    def __init__(self):
        self.new_urls = []
        self.old_urls = []

    def add_new_url(self, new_url):
        if new_url is None or new_url in self.new_urls or new_url in self.old_urls:
            return
        self.new_urls.append(new_url)
    def has_new_url(self):
        if self.new_urls is None or len(self.new_urls) == 0:
            return False
        else:
            return True
    def add_new_urls(self,new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)
    def get_new_url(self):
        new_url= self.new_urls.pop()
        self.old_urls.append(new_url)
        return new_url



