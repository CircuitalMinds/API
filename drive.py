from utils import get_json, save_json, join, listdir, stat, getmtime, ctime, isdir
from werkzeug.utils import secure_filename


class Storage:
    path = "./storage"
    directory = get_json(path, "directory")
    folder_types = {
        "data": ["json", "yml", "txt"],
        "videos": ["mp4", "mp3", "wmv", "mkv"],
        "pictures": ["jpg", "png", "svg", "gif", "jpeg"],
        "scripts": ["py", "js", "css", "sqlite3", "", "sh"],
        "documents": ["html", "pdf", "md", "markdown", "ipynb"]
    }
    folders = list(filter(lambda x, path=path: isdir(join(path, x)), listdir(path)))
    for name in folders:
        directory["folders"][name] = []

    def __init__(self):
        self.update()

    def get(self, filename):
        data = {}
        datatype = filename.split('.')[-1]
        not_found = {"response": f"filename with name {filename} not found"}
        folder = list(filter(
            lambda x: datatype in self.folder_types[x], self.folder_types
        ))
        if folder:
            folder_name = folder[0]
            if list(filter(
                lambda x: x["filename"] == filename, self.directory["folders"][folder_name]
            )):
                data.update({
                    "filename": filename, "path": join(self.path, folder_name, filename)
                })
                return data
            else:
                return not_found
        else:
            return not_found

    def upload(self, file):
        name = file.__dict__["filename"]
        if name:
            filename = secure_filename(filename=name)
            datatype = filename.split('.')[-1]
            folder = list(filter(
                lambda x: datatype in self.folder_types[x], self.folder_types
            ))
            file_path = join(self.path, join(folder[0], filename) if folder else filename)
            file.save(file_path)
            self.update()
            return {"response": f"{filename} uploaded to {file_path}"}
        else:
            return {"response": "No selected file"}

    def update(self):
        total_size = 0.0
        for name in self.folders:
            folder_path = join(self.path, name)
            folder_content = []
            for filename in listdir(folder_path):
                file_path = join(folder_path, filename)
                size = stat(file_path).st_size * 1024 * 10e-10
                total_size += size
                date = ctime(getmtime(file_path))
                folder_content.append({"filename": filename, "size": size, "date": date})
            self.directory["folders"][name] = folder_content
        self.directory["total_size"] = total_size
        save_json(self.path, "directory", self.directory)
