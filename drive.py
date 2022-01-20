from utils import join, Dumper
from directory import Directory
from werkzeug.utils import secure_filename
from flask import send_file, jsonify, redirect, url_for
storage_folder = Directory.fpath["storage"]


class Data:
    path = join(storage_folder, "data")
    datatypes = ["json", "yml", "txt"]
    files, dirs = [], []


class Documents:
    path = join(storage_folder, "documents")
    datatypes = ["html", "pdf", "md", "markdown", "ipynb"]
    files, dirs = [], []


class Pictures:
    path = join(storage_folder, "pictures")
    datatypes = ["jpg", "png", "svg", "gif", "jpeg"]
    files, dirs = [], []


class Videos:
    path = join(storage_folder, "videos")
    datatypes = ["mp4", "mp3", "wmv", "mkv"]
    files, dirs = [], []


class Scripts:
    path = join(storage_folder, "scripts")
    datatypes = ["py", "js", "css", "sqlite3", "sh"]
    files, dirs = [], []


class Storage:
    path = storage_folder
    folders = ["data", "documents", "pictures", "videos", "scripts"]
    args = {
        "get"
    }

    def __init__(self):
        self.data = Data
        self.documents = Documents
        self.pictures = Pictures
        self.videos = Videos
        self.scripts = Scripts
        self.update()

    def route(self, method, request_data):
        if method == "POST":
            files = request_data.files.getlist("files[]")
            for fi in files:
                self.upload(fi)
            return redirect(url_for("home"))
        else:
            file_data = self.get(request_data["filename"])
            if all([key in file_data for key in ("filename", "path")]):
                return send_file(file_data["path"], download_name=file_data["filename"])
            else:
                return jsonify(file_data)

    def update(self):
        data = {}
        for i in self.folders:
            data[i] = {}
            folder = self.__dict__[i]
            for key, value in Directory.get_contents(folder.path).items():
                data[i][key] = value
                if key == "files":
                    folder.files.extend(value)
                else:
                    folder.dirs.extend(value)
        Dumper.write_json(join(self.path, "directory.json"), data)
        return
    
    def get(self, filename):
        data = {}
        not_found = {"response": f"filename with name {filename} not found"}
        for i in self.folders:
            folder = self.__dict__[i]
            file_data = list(filter(lambda x: x["name"] == filename, folder.files))
            if file_data:
                data.update(file_data[0])
                return data
        return not_found

    def upload(self, file):
        name = file.__dict__["filename"]
        if name:
            filename = secure_filename(filename=name)
            datatype = filename.split('.')[-1]
            path = self.path
            for i in self.folders:
                folder = self.__dict__[i]
                if datatype in folder.datatypes:
                    path = folder.path
            file_path = join(path, filename)
            file.save(file_path)
            self.update()
            return {"response": f"{filename} uploaded to {file_path}"}
        else:
            return {"response": "No selected file"}
