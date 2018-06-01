import tornado.ioloop
import tornado.web

users = {"sennhvi": "123456"}


class SysStatusHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("user"):
            self.redirect("/login")
            return
        if self.get_argument("type") == "processes":
            com = [["pstree"], ["top", "-bn1"]]
        elif self.get_argument("type") == "system":
            com = [["uname", "-a"], ["uptime"]]
        elif self.get_argument("type") == "syslog":
            com = [["tail", "-n100", "/var/log/syslog"]]
        elif self.get_argument("type") == "storage":
            com = [["df", "-h"], ["free"]]
        elif self.get_argument("type") == "network":
            com = [["ifconfig"]]
        else:
            com = [["df", "-h"], ["free"], ["pstree"], ["top", "-bn1"], ["ifconfig"],
                   ["uname", "-a"], ["uptime"], ["tail", "/var/log/syslog"]]

        self.render("sysstatus-template.html", commands=com, join=join_all)


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login-template.html")

    def post(self):
        print(self.get_argument("name"))
        print(self.get_argument("password"))
        if self.get_argument("name") in users.keys() \
                and users[self.get_argument("name")] == self.get_argument("password"):
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/sysstatus?type=system")
            print("exe login")
        else:
            self.render("login-fail.html")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user")
        self.render("logout-template.html")

# define a function and pass its name to SysStatusHandler as argument
def join_all(lst):
    return ' '.join(lst)


if __name__ == "__main__":
    application = tornado.web.Application(
        [
            (r"/login", LoginHandler),
            (r"/sysstatus", SysStatusHandler),
            (r"/logout", LogoutHandler),
        ], cookie_secret="go_get_some_books"
    )
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
