#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/25 8:11
# @Author  : lemonxug
# @Site    : 
# @File    : modder_main.py
# @Software: PyCharm
from mod_fsc import oracle_connector, file_reader, sql_parser, html_outputer

class Modder_Main(object):
    def __init__(self):
        self.connector = oracle_connector.DbConnector()
        self.reader = file_reader.FileReader()
        self.parser = sql_parser.SqlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def mod(self, db_infor):
        try:
            conn, cursor = self.connector.connect(db_infor)
            # file_data = self.reader.get_data()
            file_data = self.reader.get_dir_data()
            old_data, new_data = self.parser.parse(cursor, file_data)
        finally:
            conn.commit()
            self.connector.close(cursor, conn)
        self.outputer.collect_data(old_data, new_data)
        self.outputer.output_html()
        self.reader.move_file()


if __name__ == "__main__":
    db_infor = 'DYKMESV2/DYKMESV2@10.125.16.103:1521/DYKMESV2'
    # filename = '20160819.csv'
    # filename = u'UC 二工厂GMES需调整信息20160819.xlsx'
    obj_modder = Modder_Main()
    obj_modder.mod(db_infor)
    
    

