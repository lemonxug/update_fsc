#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/25 8:23
# @Author  : lemonxug
# @Site    : 
# @File    : sql_parser.py
# @Software: PyCharm
import cx_Oracle

class SqlParser(object):

    def _get_db_data(self, cursor, file_data):
        old_data = []
        for line in file_data:
            sql = 'select prod_ssp from v_spec_ma where wo_ser=\'%s \' ' % line[0]
            tem = cursor.execute(sql)
            for line in tem.fetchone():
                old_data.append(line)
        return old_data

    def _modify_db_data(self, cursor, file_data):
        for line in file_data:
            sql =  'update v_spec_ma set prod_ssp=\'      %s   %s   \' where wo_ser=\'%s\'' % (line[1], line[2], line[0])
            cursor.execute(sql)
        return self._get_db_data(cursor, file_data)

    def parse(self, cursor, file_data):
        old_data = self._get_db_data(cursor, file_data)
        new_data = self._modify_db_data(cursor, file_data)

        return old_data, new_data
        
    
        






