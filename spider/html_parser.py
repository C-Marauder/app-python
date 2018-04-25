import requests

from bs4 import BeautifulSoup


class Parser:
    def parse(self, html, encode):
        data_list = []
        soup = BeautifulSoup(html, 'html.parser', from_encoding=encode)
        soup.find_next()
        #找出导航信息所在标签
        nav_div = soup.find('div', 'TagPicList')
        if nav_div is not None:
            nav_li_list = nav_div.find_all('li')
            for nav_li in nav_li_list:
                title = nav_li.find('img')['alt']
                url = nav_li.find('h2','H30').find('a')['href']
                data_list.append({'url': url, 'nextPage': None, 'data': title, 'type': 'nav'})
        else:
            #位置信息所在的div
            position_a_list = soup.find('div', 'position')
            relative_path = ''
            page_id = ''
            if position_a_list is not None:
                #相对位置的地址
                a_position = position_a_list.find('a',text='TAG')
                if a_position is not None:
                    relative_path = a_position['href']
                    page_id = a_position.find_next('a').text
            ul = soup.find('ul', id='Tag_list')
            if ul is not None:
                #下一页的a标签
                next_page = soup.find('div', 'NewPages').find('a', text='下一页')
                # 该页面的id
                a = ul.find_all('a')
                image_list = ul.find_all('img')
                for image in image_list:
                    data_list.append({'url': a[image_list.index(image)]['href'], 'data': {
                        'id': page_id,
                        'imageSrc': image['src'],
                        'title': image['alt'],
                        'width': image['width'],
                        'height': image['height']
                    }, 'nextPage': relative_path+next_page['href'], 'type': 'list'})
            else:
                image_detail = soup.find('div', id='picBody').find('img')
                next_page_url = soup.find('li', id='nl').find('a')['href']
                data_list.append({'url': None, 'nextPage': relative_path+next_page_url,'data': {'id': image_detail['alt'], 'imageSrc': image_detail['src']}, 'type': 'detail'})

        return data_list
    def parseAll(self,f,content,encoding):

        soup = BeautifulSoup(content, 'html.parser', from_encoding=encoding)
        return f(soup)
