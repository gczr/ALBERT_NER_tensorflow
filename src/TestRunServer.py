# -*- coding: utf-8 -*-

import os
import json
import time
import pickle
import traceback

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

# tornado高并发
import tornado.web
import tornado.gen
import tornado.concurrent
from concurrent.futures import ThreadPoolExecutor

# 定义端口为12306
define("port", default=12306, help="run on the given port", type=int)
#define("port", default=12312, help="run on the given port", type=int)



class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('abc')


# 主函数
def main():
    # 开启tornado服务
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[
					  (r'/test', TestHandler)
                     ], #网页路径控制
           )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

main()