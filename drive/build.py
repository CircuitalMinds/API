from libs.utils import base_path, iter_folder
from .view import documents, videos, pictures, trash
from flask import send_file
from werkzeug.utils import secure_filename
from json import dumps
from pathlib import Path


def getinfo(fpath):
    class Info:
        path = Path(str(fpath)).joinpath("info.json")
        total_size = 0.0
        content = dict()
        keys = ("total_size", "content")
        config = dict(indent=4, sort_keys=True, ensure_ascii=False)

        def __init__(self):
            self.data = dict()

        def update(self):
            self.data = {key: getattr(self, key) for key in self.keys}
            self.path.open("w").write(dumps(self.data, **self.config))
    return Info()


class Folder:

    def __init__(self, rpath):
        self.path = Path(base_path).joinpath(f"application/drive/{rpath}")
        self.name = self.path.name
        self.info = getinfo(self.path)
        self.getdata()

    def getdata(self):
        self.reset_data()
        self.info.content.update(iter_folder(self.path))
        self.info.update()
        return self.info.data

    def reset_data(self):
        self.info = getinfo(self.path)

    def save_file(self, data):
        for file in data:
            filepath = self.path.joinpath(secure_filename(file.filename))
            if not filepath.is_file():
                file.save(str(filepath))

    def getfile(self, filepath):
        file = self.path.joinpath(filepath)
        return send_file(
            str(file), download_name=file.name
        )


def init_drive(app):
    trash(app, Folder("trash"))
    for view in (documents, videos, pictures):
        view(app, Folder(f"storage/{view.__name__}"))




r'''

def getinfo(fpath):

            dirs=[di for di in dir_paths if di not in ignore and not di.startswith(".")],
    class Info:
        path = Path(str(fpath)).joinpath("info.json")
        available_space = True
        total_size = 0.0
        content = None
        ready_to_push = True
        keys = ("available_space", "total_size", "content", "ready_to_push")
        config = dict(indent=4, sort_keys=True, ensure_ascii=False)

        def __init__(self):
            self.data = dict()

        def update(self):
            self.checkout()
            self.data = {key: getattr(self, key) for key in self.keys}
            self.path.open("w").write(dumps(self.data, **self.config))

        def checkout(self):
            if not self.content:
                return
            if self.total_size > 9.5e2:
                self.available_space = False
                if self.total_size > 1.05e3:
                    self.ready_to_push = False
                    return
            for x in self.content:
                if x.get("size") > 53.0:
                    self.ready_to_push = False
                    break

    return Info()


class Container:

    def __init__(self, root, name):
        self.name = name
        self.path = Path(root).joinpath(self.name)
        self.info = getinfo(self.path)

    def reset_data(self):
        content = self.info.content
        content.clear()
        self.info = getinfo(self.path)
        self.info.content = content

    def save_file(self, folder):
        if self.path.joinpath(folder).is_dir():
            files = request.files.getlist('files[]')
            for file in files:
                file.save(self.path.joinpath(
                    folder, secure_filename(file.filename)
                ))

    def getfile(self, filepath):
        file = self.path.joinpath(filepath)
        return send_file(
            file.absolute(), download_name=file.name.strip()
        )


class Videos(Container):
    folders = list(i.name for i in videos_path.iterdir())

    def __init__(self, folder):
        super().__init__(
            videos_path, folder
        )
        self.url_root = f"https://github.com/circuitalmynds/music_{folder}/blob/main/videos"
        self.info.content = []
        self.getdata()

'''
