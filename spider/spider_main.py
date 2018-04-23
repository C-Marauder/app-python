from spider import html_downloader, html_parser, url_manager, data_manager


class Spider:
    def __init__(self, root_url):
        self.root_url = root_url
        dataManager = data_manager.DataManager()
        manager = url_manager.UrlManager(root_url)
        downloader = html_downloader.Downloader()
        html, encode = downloader.download(root_url)
        print(encode)
        parser = html_parser.Parser()
        nav_urls, nav_list = parser.parse_nav(html, encode)
        dataManager.save(nav_list,'nav')
        # for nav in nav_list:
            # nav_text = nav.decode('utf-8').encode(encode)
            # print(nav+'---')
        # while len(manager.urls) != 0:
        #     new_url = manager.get_new_url()
        #     html, encode = downloader.download()
        #
        #     parser.parse()


if __name__ == "__main__":
    spider_url = 'http://www.mm131.com/'
    Spider(spider_url)