from fmod import Obj, Dir
from werkzeug.utils import secure_filename
from flask import send_file, jsonify, redirect, url_for
info = Obj(Dir.join("storage", "info.json"))


class Storage:

    class Data:
        name = "data"
        files, dirs = [], []
        datatypes = ["json", "yml", "txt"]

    class Documents:
        name = "documents"
        files, dirs = [], []
        datatypes = ["html", "pdf", "md", "markdown", "ipynb"]

    class Pictures:
        name = "pictures"
        files, dirs = [], []
        datatypes = ["jpg", "png", "svg", "gif", "jpeg"]

    class Videos:
        name = "videos"
        files, dirs = [], []
        datatypes = ["mp4", "mp3", "wmv", "mkv"]

    class Scripts:
        name = "scripts"
        files, dirs = [], []
        datatypes = ["py", "js", "css", "sqlite3", "sh"]

    def __init__(self):
        self.folders = ("Data", "Documents", "Pictures", "Videos", "Scripts")
        for i in self.folders:
            self.__setattr__(i, self.__getattribute__(i)())
        self.update()

    def route(self, method, request_data):
        if method == "POST":
            files = request_data.files.getlist("files[]")
            for fi in files:
                self.upload(fi)
            return redirect(url_for("home"))
        else:
            filename = request_data.get("filename")
            if filename:
                file_data = self.get(filename)
                if all([key in file_data for key in ("name", "path")]):
                    return send_file(file_data["path"], download_name=file_data["name"])
                else:
                    return jsonify(file_data)
            else:
                return jsonify(info.data)

    def update(self):
        info.data["total_size"] = 0.0
        for i in self.folders:
            name = self.__dict__[i].name
            contents = Dir.contents("storage", name)
            info.data["folders"][name] = contents
            for x, y in contents.items():
                info.data["total_size"] += sum([float(yi["size"]) for yi in y])
                self.__dict__[i].__dict__[x] = y
        info.save()
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
            path = Dir.join("storage")
            for i in info.data["folders"]:
                folder = self.__dict__[i]
                if datatype in folder.datatypes:
                    path = folder.path
            file_path = Dir.join(path, filename)
            file.save(file_path)
            self.update()
            return {"response": f"{filename} uploaded to {file_path}"}
        else:
            return {"response": "No selected file"}
