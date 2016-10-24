#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/25 8:40
# @Author  : lemonxug
# @Site    : 
# @File    : file_reader.py
# @Software: PyCharm
import csv
import xlrd
import sys
import os
import shutil

path1 = os.path.join(os.getcwd(), 'fsc_data')
# path1 = os.path.join(sys.path[0], 'fsc_data')
path = path1.decode('gbk')

# dir = r'F:\Work Record\SQL_FSC 变更\mod_fsc\fsc_data'.decode('gbk')
# os.system("explorer.exe %s" % dir.encode('gb2312'))

class FileReader(object):
    def __init__(self):
        self.path = path
        self.data = []
    def get_dir_data(self, dir=path):

        for file in os.listdir(dir):
            filename = os.path.join(dir,file)
            for line in self.get_data(filename):
                self.data.append(line)
        # return  os.listdir(dir)
        return self.data
    def get_data(self,filename):
        items = []
        # filelist = self.get_filelist()

        if len(filename) == 0 :
            raise "there is no file!"
        # for filename in filelist:
        if 'csv' in filename:
            data = self.read_csv(filename)
        if 'xlsx' in filename:
            data = self.read_excel(filename)
        items = [line for line in data]
        return items

    def read_csv(self,filename):
        fsc = file(os.path.join(path, filename), 'rb')
        # fsc = file(filename, 'rb')
        data = csv.reader(fsc)
        return data

    def read_excel(self, filename):
        data = []
        workbook = xlrd.open_workbook(os.path.join(path, filename))
        # workbook = xlrd.open_workbook(filename)
        sheet1 = workbook.sheet_by_index(0)
        for i in range(4,sheet1.nrows - 1):
            line = []
            item1 = sheet1.cell(i,1).value[:9].encode('utf-8')
            item2 = sheet1.cell(i,3).value[6:13].encode('utf-8')
            item3 = sheet1.cell(i,3).value[14:].encode('utf-8')
            line = [item1, item2, item3]
            data.append(line)

        return data

    def move_file(self):
        souceDir = os.path.join(os.getcwd(), 'fsc_data')
        targetDir = os.path.join(os.getcwd(), 'record')
        for file in os.listdir(souceDir):
            shutil.move(os.path.join(souceDir,file), os.path.join(targetDir,file))
