import requests

from bs4 import BeautifulSoup


class Parser:

    def parseAll(self,f,content,encoding):

        soup = BeautifulSoup(content, 'html.parser', from_encoding=encoding)
        return f(soup)
