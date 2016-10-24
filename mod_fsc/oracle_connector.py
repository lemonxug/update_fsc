#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/25 8:13
# @Author  : lemonxug
# @Site    : 
# @File    : oracle_connector.py
# @Software: PyCharm
import cx_Oracle

class DbConnector(object):

    def connect(self, db_infor):
        if db_infor is None:
            return None
        conn = cx_Oracle.connect(db_infor)
        cursor = conn.cursor()
        return conn, cursor

    def close(self, cursor, conn):
        cursor.close ()
        conn.close ()