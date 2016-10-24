#! C;\\python python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/25 8:41
# @Author  : lemonxug
# @Site    : 
# @File    : html_outputer.py
# @Software: PyCharm
from datetime import *
import sys

class HtmlOutputer(object):
    def __init__(self):
        self.datas = {}

    def collect_data(self, old_data, new_data):
        self.datas['old'] = old_data
        self.datas['new'] = new_data

    def output_html(self):
        path = sys.path[0] + '/report_html/'
        dt = datetime.now()
        html = open(path + r'%s.html' % date.today(), 'a')
        # html = open(r'%s.html' % dt.strftime('%c'), 'w')
        html.write("""
        <html>
        <head>
          <title>%s_FSC_CHANGE</title>
          <meta charset="utf-8">
        </head>
        <body>
        """ % date.today())
        html.write('<p ><font size="10" color="red">%s</font></p>'  % dt.strftime('%c'))
        html.write('<table border="1">')
        html.write("<tr>")
        html.write("<th>old</th>" )
        html.write("<th>new</th>" )
        html.write("</tr>")

        for i in range(len(self.datas['old'])):
            html.write("<tr><td>%s</td><td>%s</td></tr>" % (self.datas['old'][i], self.datas['new'][i]))

        html.write('</table>')
        html.write('</body></html>')
        html.close()