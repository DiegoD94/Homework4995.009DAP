import tornado.ioloop
import tornado.web
import logging


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

class MyNameHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Ding Han is my name!")


class Application(tornado.web.Application):
    def __init__(self):
        app_settings = {
            'default_handler_args': dict(status_code=404),
        }

        app_handlers = [
            (r'^/$', MainHandler),
            (r'^/name$', MyNameHandler),
        ]

        super(Application, self).__init__(app_handlers, **app_settings)


if __name__ == "__main__":
    port = 8000
    address = '0.0.0.0'
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)
    logging.info('starting event logger on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()