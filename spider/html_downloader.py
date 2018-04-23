import requests


class Downloader:

    def download(self, new_url):
        response = requests.get(new_url)
        html = response.content
        encode = response.encoding
        return html, encode

