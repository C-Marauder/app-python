from spider.html_parser import Parser


class LadyParser(Parser):

    def parser_list(self,soup):
        # 位置信息所在的div
        position_a = soup.find('div', 'position').find_all('a')

        relative_path = position_a[0]['href']
        page_id = position_a[-1].text

        li_list = soup.find('ul', id='Tag_list').find_all('li')
        dataList = []
        taskList = []
        next_page = soup.find('a', text='下一页')['href']

        for li in li_list:
            del li['div']
            a = li.find('a')
            img = a.find('img')
            if next_page is not None:
                taskList.append({'currentPage':{'url':a['href'],'type':'detail'},'nextPage':{'url':relative_path+next_page,'type':'list'}})
                dataList.append({'data':{
                    'id':page_id,
                    'picUrl':img['src'],
                    'title':a['title'],
                    'width':img['width'],
                    'height':img['height']}})
            else:
                taskList.append({'currentPage':{'url':a['href'],'type':'detail'},'nextPage':None})
                dataList.append({'data': {
                    'id': page_id,
                    'picUrl': img['src'],
                    'title': a['title'],
                    'width': img['width'],
                    'height': img['height']}})
            print(img['src'] + '---' + a['title'])
        return dataList, taskList

    def parse_detail(self,soup):
        dateList = []
        taskList = []
        image = soup.find('p', align='center').find('img')
        title = soup.find('h1', 'articleV4Tit').text
        position_a = soup.find('div', 'position').find_all('a')[-1]
        # count = len(position_a_tag)
        position_url = position_a['href'] + '2017/'
        nextPageUrl = position_url + soup.find('a', text='下一页')['href']
        if nextPageUrl.endswith('.html'):
            taskList.append({'currentPage':None,'nextPage':{'url':nextPageUrl,'type':'detail'}})
            dateList.append({'data':{'id':title,'picUrl':image['src']},})
        else:
            dateList.append({'data':{'id':title,'picUrl':image['src']},})

        print(image['src'] + '---' + nextPageUrl + '----' + title)
        return dateList, taskList