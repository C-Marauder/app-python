import pymysql


class DataManager:
    NAV_SQL_INSERT = "insert into t_app_nav values('%d', '%s', '%s')"
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect("localhost", "root", "qq112358", "lady")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
    def save(self, data_list, type):
        sql = ''
        if type == 'nav':
            sql = self.NAV_SQL_INSERT
        count = 0
        for data in data_list:
            print(data+'---')
            count = count+ 1
            # try:
            self.cursor.execute(sql % \
                         (count, data, None))
            self.db.commit()

        # except:
            self.db.rollback()

        self.db.close()
