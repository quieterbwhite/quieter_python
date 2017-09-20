# -*- coding=utf-8 -*-

import tornado.web
import tornaod.ioloop

class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.write("hello sweet dream")

if __name__ == "__main__":

    app = tornado.web.application([(r"/", IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()