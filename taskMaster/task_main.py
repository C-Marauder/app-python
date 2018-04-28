from queue_manager import master_queue
from spider import html_parser, html_downloader
class TaskManager:
    def __init__(self):
        self.__root_url = 'http://www.27270.com/ent/meinvtupian/'

    def __downloadContent(self):
        htmlDownloader = html_downloader.Downloader()
        content, encoding  = htmlDownloader.download(self.__root_url)
        return content, encoding

    def __parseHtml(self,soup):
        data_list = []
        nav_div = soup.find('div', 'TagPicList')
        nav_li_list = nav_div.find_all('li')
        for nav_li in nav_li_list:
            url = nav_li.find('h2', 'H30').find('a')['href']
            data_list.append({'currentPage':{'url': url, 'type': 'list'},'nextPage':None})

        return data_list
    def get_tasks(self):
        content , encoding = self.__downloadContent()
        htmlParser = html_parser.Parser()
        return htmlParser.parseAll(self.__parseHtml, content, encoding)
if __name__ == '__main__':
    tasks = TaskManager().get_tasks()
    taskCount = len(tasks)
    taskManager = master_queue.QueueManager(address=('192.168.2.75',5000),authkey=b'123',taskCount=taskCount)
    taskManager.dispatch_tasks(tasks)



