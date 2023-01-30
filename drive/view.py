from flask import request


def response(app, folder, filename):
    if request.method == "POST":
        folder.save_file(request.files.getlist('files[]'))
        return app.getjson(folder.getdata())
    elif filename:
        return folder.getfile(filename)
    else:
        return app.getjson(folder.getdata())


def documents(app, folder):
    @app.route("/drive/", methods=["GET", "POST"])
    @app.route("/drive/documents/", methods=["GET", "POST"])
    @app.route("/drive/documents/<filename>/", methods=["GET", "POST"])
    def get_documents(filename=None):
        return response(app, folder, filename)


def videos(app, folder):
    @app.route("/drive/", methods=["GET", "POST"])
    @app.route("/drive/videos/", methods=["GET", "POST"])
    @app.route("/drive/videos/<filename>/", methods=["GET", "POST"])
    def get_videos(filename=None):
        return response(app, folder, filename)


def pictures(app, folder):
    @app.route("/drive/", methods=["GET", "POST"])
    @app.route("/drive/pictures/", methods=["GET", "POST"])
    @app.route("/drive/pictures/<filename>/", methods=["GET", "POST"])
    def get_pictures(filename=None):
        return response(app, folder, filename)


def trash(app, folder):
    @app.route("/drive/", methods=["GET", "POST"])
    @app.route("/drive/trash/", methods=["GET", "POST"])
    def get_trash():
        return app.getjson(folder.getdata())
