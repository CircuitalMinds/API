from utils import join, isdir, isfile
from os import listdir, stat
from os.path import getmtime
from time import ctime


class Directory:
    fpath = dict(
        database="./database",
        storage="./storage"
    )
    
    @staticmethod
    def ls(path, *paths):
        if paths:
            return list(map(
                lambda j: listdir(j), filter(lambda i: isdir(i), (path, ) + paths)
            ))
        else:
            return listdir(path) if isdir(path) else []            

    @staticmethod
    def dir_date(path, *paths):
        if paths:
            return list(map(
                lambda j: ctime(getmtime(j)), filter(lambda i: isdir(i) or isfile(i), (path, ) + paths)
            ))
        else:
            return ctime(getmtime(path)) if isdir(path) or isfile(path) else None

    @staticmethod
    def dir_size(path, *paths):
        factor = 1024 * 10e-10
        if paths:
            return list(map(
                lambda j: stat(j).st_size * factor, filter(lambda i: isdir(i) or isfile(i), (path,) + paths)
            ))
        else:
            return stat(path).st_size * factor if isdir(path) or isfile(path) else None

    @classmethod
    def get_contents(cls, path):
        data = {"files": [], "dirs": []}
        for i in cls.ls(path):
            path_i = join(path, i)
            data_i = {"name": i, "path": path_i, "date": cls.dir_date(path_i), "size": cls.dir_size(path_i)}
            if isfile(path_i):
                data["files"].append(data_i)
            else:
                data["dirs"].append(data_i)
        return data
