import tornado.web


class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, word")
