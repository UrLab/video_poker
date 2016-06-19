from tornado.ioloop import IOLoop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("the game is at /api/game buddy")


class GameHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GET - Welcome to the Video Poker")

    def post(self):
        self.write("POST - Mofo")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/api/video_poker/?", GameHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8000)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()