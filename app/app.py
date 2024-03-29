import os
import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler
from pywebio.output import *
from pywebio import STATIC_PATH

TEST_VAR = os.getenv('TEST_VAR')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def task_func() -> None:
    put_markdown("""
        # Year!!!!
        - 1
        - 2
        - 3
        os.getenv("TEST_VAR")
    """)
    put_text(TEST_VAR)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/tool", webio_handler(task_func)),  # `task_func` is PyWebIO task function
    ])
    application.listen(port=8080, address='0.0.0.0') # run python3 app.py

    # application.listen(port=8080, address='localhost')  # run python3 app.py

    tornado.ioloop.IOLoop.current().start()
