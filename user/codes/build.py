def get_userdata(**form):
    userdata = dict()
    for key in ("email", "password"):
        if key in form:
            userdata[key] = form[key]
        else:
            return
    return userdata


def getmethods(*opts):
    return [opt.upper() for opt in opts]


class Admin:

    @staticmethod
    def view(app):

        @app.route("/user/", methods=getmethods("get", "post"))
        @app.route("/user/admin/", methods=getmethods("get", "post"))
        def login(path=None):
            if path:
                return app.getjson(app.getdata.form)
            else:
                return app.getjson(dict(user="admin"))


