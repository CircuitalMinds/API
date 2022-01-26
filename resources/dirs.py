from os.path import join, isdir, isfile, getctime
from os import listdir, stat, system, walk, mkdir, remove
from zipfile import ZipFile
from subprocess import getoutput
import time


class Dir:

    def __init__(self, path):
        self.path = path
        
    def join(self, *paths):
        return join(self.path, *paths)
    
    def isfile(self, *paths):
        return isfile(self.join(*paths))
    
    def isdir(self, *paths):
        return isdir(self.join(*paths))
    
    def ls(self, *paths):
        return listdir(self.join(*paths)) if self.isdir(*paths) else []

    def open_file(self, *paths):
        return open(self.join(*paths)).read() if self.isfile(*paths) else ""

    def save_file(self, *paths, data):
        with open(self.join(*paths), "w") as f:
            f.write(data), f.close()
        return
        
    def date(self, *paths):
        if self.isfile(*paths) or self.isdir(*paths):
            return time.ctime(getctime(self.join(*paths)))
        else:
            return None

    def size(self, *paths):
        factor = 1024 * 10e-10
        if self.isfile(*paths):
            return stat(self.join(*paths)).st_size * factor
        elif self.isdir(*paths):
            return sum([stat(self.join(*paths, i)).st_size * factor for i in self.ls(*paths)])
        else:
            return None

    def contents(self, *paths):
        data = {"files": [], "dirs": []}
        if self.isdir(*paths):
            for i in self.ls(*paths):
                dpath = self.join(*paths, i)
                data_i = {
                    "name": i,
                    "path": dpath,
                    "date": self.date(dpath),
                    "size": "{:.4f}".format(self.size(dpath))
                }
                if isfile(dpath):
                    data["files"].append(data_i)
                else:
                    data["dirs"].append(data_i)
        return data

    def copy_files(self, from_path, to_path, *ignores):
        if self.isdir(from_path) and self.isdir(to_path):
            for i in self.ls(from_path):
                if self.isfile(from_path, i) and i not in ignores:
                    system(f"cp {self.join(from_path, i)} {self.join(to_path, i)}")
        return

    def copy_folders(self, from_path, to_path, *ignores):
        if self.isdir(from_path) and self.isdir(to_path):
            for i in self.ls(from_path):
                if self.isdir(from_path, i) and i not in ignores:
                    system(f"cp -R {self.join(from_path, i)} {self.join(to_path)}")
        return

    def create_folder(self, *paths):
        if not self.isdir(*paths):
            mkdir(self.join(*paths))
        return

    def create_zip(self, folder_path):
        if isdir(self.join(folder_path)):
            zip_path = folder_path + ".zip"
            with ZipFile(zip_path, 'w') as zipObj:
                for folderName, sub_folders, filenames in walk(folder_path):
                    for filename in filenames:
                        filePath = Dir.join(folderName, filename)
                        zipObj.write(filePath)
            return {"filename": zip_path.split("/")[-1], "path": zip_path}
        else:
            return {"response": "folder not found"}

    def remove_zip(self, zip_path):
        remove(self.join(zip_path))
        return

    def get_info_zip(self, zip_path):
        name = zip_path.split('/')[-1]
        folder_path = self.join(zip_path.replace(f"/{name}", ""))
        data = []
        str_data = getoutput(" && ".join([f"cd {folder_path}", "python -m zipfile -l ./{name}"])).splitlines()[1:]
        for s in str_data:
            y = s.split()
            print(y)
            data.append({
                "filename": y[0],
                "date": " ".join([y[1].replace("-", "/"), y[2]]),
                "size": y[3]
            })
        print(data)
        return data
