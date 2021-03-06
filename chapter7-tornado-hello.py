import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
    any class for processing website must
    inherit from tornado.web.RequestHandler which provide all basic features
    define class for creating website
    """

    def get(self):
        self.write("<!DOCTYPE html><head><title>" +
                   "Hello World!</title></head>" +
                   "<body>Hello World</body>")


class HelloHandler(tornado.web.RequestHandler):
    def get(self, name_in):
        self.name = name_in
        self.render("./chapter7-hello-template.html",
                    name=self.name)


class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./chapter7-post-form.html")

    def post(self, *args, **kwargs):
        # .html.self.get_argument() get user input data
        self.render("./chapter7-hello-template.html", name=self.get_argument("name"))


# create a Tornado web application and set up its options
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),  # a list of tuple defining class processing page.i.e. MainHandler process root page
        (r"/hello/(.*)", HelloHandler),
        (r"/form/", FormHandler),
    ], )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
