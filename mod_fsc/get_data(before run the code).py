#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/1 9:44
# @Author  : lemonxug
# @Site    : 
# @File    : get_data(before run the code).py
# @Software: PyCharm
import os
from file_reader import *
import shutil

fr = FileReader()
# souceDir = os.path.join(os.getcwd(), 'fsc_data')
# targetDir = os.path.join(os.getcwd(), 'record')
# for file in os.listdir(souceDir):
#     data = []
#     filename = os.path.join(souceDir,file)
#     data  = fr.get_data(filename)
#     for line in data:
#         print line
data = fr.get_dir_data()
for line in data:
    print line