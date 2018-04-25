import pymysql


class DataManager:
    NAV_SQL_INSERT = "insert into t_app_nav values('%d', '%s', '%s')"
    LIST_SQL_INSERT = "insert into t_app_list VALUES('%s','%s','%s','%s','%s','%s','%s') "
    DETAIL_SQL_INSERT = "insert into t_app_detail VALUES('%s','%s','%s','%s')"
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect("localhost", "root", "qq112358", "lady", charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
    def save(self, data_list):
        # sql = ''

        count = 0
        for data in data_list:
            print(data)
            data_type= data['type']

            count = count+ 1
            try:
                if data_type == 'nav':
                    sql = self.NAV_SQL_INSERT
                    self.cursor.execute(sql % \
                             (count, data['data'], None))
                if data_type == 'list':
                    sql = self.LIST_SQL_INSERT
                    data_item = data['data']
                    self.cursor.execute(sql % \
                                        (data_item['id'],data_item['title'],data_item['imageSrc'], data_item['width'],data_item['height'], None,None))
                if data_type == 'detail':
                    sql = self.DETAIL_SQL_INSERT
                    data_item = data['data']
                    self.cursor.execute(sql % \
                                        (data_item['id'], data_item['imageSrc'],None,None))

                self.db.commit()

            except:
                self.db.rollback()

        #self.db.close()
