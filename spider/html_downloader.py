import chardet
import requests


class Downloader:

    def download(self, new_url):
        response = requests.get(new_url)
        if response.ok:
            html = response.content
            encode = chardet.detect(html)['encoding']
            html = html.decode(encode,'ignore').encode('utf-8')
            print(response.encoding+'---'+encode)
            return html, encode

