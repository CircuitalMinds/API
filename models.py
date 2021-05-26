from sqlalchemy import Column, Integer, String, Text


def select_model(Model, name):

    class UserRegister(Model):
        user_id = Column(Integer, primary_key=True, unique=True)
        username = Column(String(50), nullable=False, unique=True)
        password = Column(String(50), nullable=False)

        args = ["username", "password"]
        repr = "user_id"
        secondary_repr = "username"

        def __init__(self, data):
            for arg in UserRegister.args:
                self.__setattr__(arg, data[arg])

        def __repr__(self):
            return '<UserRegister %r>' % self.user_id

    class Blog(Model):
        post_id = Column(Integer, primary_key=True, unique=True)
        title = Column(String(100), nullable=False, unique=True)
        content = Column(Text, nullable=False)
        date = Column(String(100), nullable=False)
        picture = Column(String(100), nullable=False)

        args = ["title", "date", "content", "picture"]
        repr = "post_id"
        secondary_repr = "title"

        def __init__(self, data):
            for arg in Blog.args:
                self.__setattr__(arg, data[arg])

        def __repr__(self):
            return '<Blog %r>' % self.post_id

    class MusicApp(Model):
        video_id = Column(Integer, primary_key=True, unique=True)
        video_title = Column(String(100), nullable=False)
        video_url = Column(String(100), nullable=False)
        video_image = Column(String(100), nullable=False)

        args = ["video_url", "video_title", "video_image"]
        repr = "video_id"
        secondary_repr = "video_title"

        def __init__(self, data):
            for arg in MusicApp.args:
                self.__setattr__(arg, data[arg])

        def __repr__(self):
            return '<MusicApp %r>' % self.video_id

    class JupyterApp(Model):
        notebook_id = Column(Integer, primary_key=True, unique=True)
        title = Column(String(100), nullable=False, unique=True)
        topic = Column(String(100), nullable=False)
        module = Column(String(100), nullable=False)
        location = Column(String(100), nullable=False)
        resources = Column(String(100), nullable=False)

        args = ["title", "topic", "module", "location", "resources"]
        repr = "notebook_id"
        secondary_repr = "title"

        def __init__(self, data):
            for arg in JupyterApp.args:
                self.__setattr__(arg, data[arg])

        def __repr__(self):
            return '<JupyterApp %r>' % self.notebook_id

    model = {"user_register": UserRegister,
             "blog": Blog,
             "jupyter_app": JupyterApp,
             "music_app": MusicApp}[name]
    return model
