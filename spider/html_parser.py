
import requests

from bs4 import BeautifulSoup


class Parser:

    def parse_nav(self, html, encode):
        soup = BeautifulSoup(html, 'html.parser', from_encoding=encode)
        nav_list = soup.find('div', 'nav').find_all('a')
        # 删除第一个
        del nav_list[0]
        nav_urls = []
        nav_text = []
        for nav in nav_list:
            nav_urls.append(nav['href'])
            nav_text.append(nav.text)
        return nav_urls, nav_text

    def parse(self, html, encode):
        soup = BeautifulSoup(html, 'html.parser', from_encoding=encode)
        images = soup.find_all('img')
        for image in images:
            print(image['src']+'---')
