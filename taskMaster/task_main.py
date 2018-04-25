from spider import html_parser, html_downloader
from taskMaster import  queue_manager
class TaskManager:
    def __init__(self):
        self.__root_url = 'http://www.27270.com/ent/meinvtupian/'
        # self__urlManager = url_manager.UrlManager()
        # self__urlManager.add_new_url(self.__root_url)
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
            data_list.append({'url': url, 'type': 'list'})

        return data_list
    def get_tasks(self):
        content , encoding = self.__downloadContent()
        htmlParser = html_parser.Parser()
        return htmlParser.parseAll(self.__parseHtml, content, encoding)
if __name__ == '__main__':
    tasks = TaskManager().get_tasks()
    queue_manager.QueueManager.register_task_and_result_id('get_task_queue','get_result_queue')
    taskManager = queue_manager.QueueManager(address=('192.168.2.75',5000),authkey=b'123')
    taskManager.taskCount = len(tasks)
    queue_manager.QueueManager.register('get_task_count', callable=lambda:taskManager.taskCount)
    taskManager.start()
    taskManager.dispatch_tasks(tasks)
    results = taskManager.get_result_queue()
    for i in range(taskManager.taskCount):
        r = results.get()
        print(r)
    taskManager.shutdown()

