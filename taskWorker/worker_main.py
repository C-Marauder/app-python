from queue_manager import worker_queue
from spider import html_downloader, url_manager, html_parser, data_manager
from taskWorker import worker_parser


class SpiderWorker():
    def __init__(self):
        self.__url_manager = url_manager.UrlManager()
        self.__html_downloader = html_downloader.Downloader()
        self.__html_parser = worker_parser.LadyParser()
        self.__data_manager = data_manager.DataManager()

    def craw(self, task):
        self.__url_manager.add_new_url(task)
        while self.__url_manager.has_new_url():
            new_job = self.__url_manager.get_new_url()
            current_page = new_job['currentPage']
            if current_page is not None:
                current_url = current_page['url']
                current_url_type = current_page['type']
                content, encoding = self.__html_downloader.download(current_url)
                if current_url_type == 'list':
                    dataList,taskList = self.__html_parser.parseAll(self.__html_parser.parser_list,content,encoding)

                else:
                    dataList,taskList = self.__html_parser.parseAll(self.__html_parser.parse_detail,content,encoding)

                self.__url_manager.add_new_urls(taskList)

            else:
                next_page = new_job['nextPage']
    
                if next_page is not None:
                    next_url = next_page['url']
                    next_url_type = next_page['type']
                    content, encoding = self.__html_downloader.download(next_url)
                    if next_url_type == 'list':
                        dataList, taskList = self.__html_parser.parseAll(self.__html_parser.parser_list, content, encoding)
                    else:
                        dataList, taskList = self.__html_parser.parseAll(self.__html_parser.parse_detail, content, encoding)

                    self.__url_manager.add_new_urls(taskList)




if __name__ == '__main__':
    worker = worker_queue.QueueManager(address=('192.168.2.75', 5000), authkey=b'123')
    worker.get_task_to_work(SpiderWorker().craw)
