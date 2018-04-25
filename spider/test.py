from spider import html_downloader, html_parser, url_manager
from bs4 import BeautifulSoup
url = 'http://www.27270.com/ent/meinvtupian/2017/226226.html'
urlManager = url_manager.UrlManager()
urlManager.add_new_url(url)
downloader= html_downloader.Downloader()
parser = html_parser.Parser()


def parse_detail(soup):
    image = soup.find('p', align='center').find('img')
    title = soup.find('h1', 'articleV4Tit').text
    position_a = soup.find('div', 'position').find_all('a')[-1]
    # count = len(position_a_tag)
    position_url = position_a['href'] + '2017/'
    nextPageUrl = position_url + soup.find('a', text='下一页')['href']
    if nextPageUrl.endswith('.html'):
        urlManager.add_new_url(nextPageUrl)
    print(image['src'] + '---' + nextPageUrl + '----' + title)

while urlManager.has_new_url():
    new_url = urlManager.get_new_url()
    html, encode = downloader.download(new_url)
    parser.parseAll(parse_detail,html,encode)