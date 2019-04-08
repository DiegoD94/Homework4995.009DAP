from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

import time

# from email_client import send_email
# from loyal_client import enroll

import tornado.gen

@tornado.gen.coroutine
def send_email(email_address):
    yield tornado.gen.sleep(5)
    raise tornado.gen.Return(True)

@tornado.gen.coroutine
def enroll(customer_id):
    yield tornado.gen.sleep(5)
    raise tornado.gen.Return(True)

class CustomerHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # create_customer(self)  # create the database entry
        customer_id = self.get_argument('customer_id')
        email_address = self.get_argument('email_address')
        email_sent, enrolled = yield [send_email(email_address), enroll(customer_id)]
        self.write('OK: email sent: {}, enrolled {}'.format(email_sent, enrolled))
        self.finish()

if __name__ == "__main__":
    handler_mapping = [
                       (r'/enroll', CustomerHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()