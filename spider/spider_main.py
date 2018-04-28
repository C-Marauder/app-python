from spider import html_downloader, html_parser, url_manager, data_manager


class Spider:
    def __init__(self):
        self.dataManager = data_manager.DataManager()
        #实例化url管理器
        self.urlManager = url_manager.UrlManager()
        #获取url
        # urlInfo = self.manager.get_new_url()
        #实例化html下载器
        self.downloader = html_downloader.Downloader()
        #根据url返回相应html和encode
        # html, encode = downloader.download(urlInfo['url'])
        #实例化html解析器
        self.parser = html_parser.Parser()
        #返回新的url和数据
        # nav_urls, nav_list = parser.parse_nav(html, encode)
        # dataManager.save(nav_list, urlInfo['type'])
        # for url in nav_urls:
        #     new_html, encode = downloader.download(url)
        #     parser.parse()
    def craw(self,root_url):
        #URL管理器添加入口url
        self.urlManager.add_new_url(root_url)
        while self.urlManager.has_new_url():
            url = self.urlManager.get_new_url()
            html, encode = self.downloader.download(url)
            data_list = self.parser.parse(html,encode)
            self.dataManager.save(data_list)
            for data in data_list:
                next_page_url = data['nextPage']
                new_url = data['url']
                if new_url is not None:
                    self.urlManager.add_new_url(data['url'])

                if next_page_url is not None:
                    self.urlManager.add_new_url(next_page_url)
#
#
#
#
# if __name__ == "__main__":
#     root_url = 'http://www.27270.com/ent/meinvtupian/'
#
#     Spider().craw(root_url)