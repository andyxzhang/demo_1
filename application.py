import os

import tornado.ioloop
import tornado.web

from src.handler.home_page import HomePageHandler

'''
    static_path: 静态文件地址
    cookie_secret: 加密cookie使用，避免XSS攻击
    xsrf_cookies: 开启xsrf防护，所有post需要添加xsrf信息用于验证
    login_url: 登录链接，添加了这一项之后，可以使用@tornado.web.authenticated
'''
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXZXGaYdkL5gEmGeJJFuYh7EQnp2ZdTP2odje=",
    "xsrf_cookies": True,
    "login_url": "/login",
}

def make_app():
    # 地址链接前面的“r”在这里还是蛮重要的，避免地址链接中有特殊字符被转义
    app = tornado.web.Application([
        (r"/", HomePageHandler),
        (r"/login", HomePageHandler),# NeedFix:之后做了专门的登录页再修改
        ], **settings)

    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(9001)
    tornado.ioloop.IOLoop.instance().start()