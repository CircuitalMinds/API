from os import stat, listdir, remove, walk
from os.path import join, isdir, isfile, getmtime
from time import ctime
from zipfile import ZipFile
from json import load, dumps
from subprocess import getoutput
folder_size = 0.0


def get_folder_data(name):
    folder_path = name if name.startswith("./") else f"./{name}"
    if isdir(folder_path):
        def folder_data(*args, **kwargs):
            xpath = join(*args)
            for key in ("files", "folders"):
                if key not in kwargs:
                    kwargs[key] = []
            for x in listdir(xpath):
                d_path = join(xpath, x)
                if isfile(d_path):
                    size = stat(d_path).st_size * 1024 * 10e-10
                    globals()["folder_size"] += size
                    date = ctime(getmtime(d_path))
                    kwargs["files"].append({"filename": x, "size": size, "date": date})
                else:
                    f_data = folder_data(d_path)
                    f_data.update({"name": x, "path": d_path.split("./")[-1]})
                    kwargs["folders"].append(f_data)
            return kwargs
        globals()["folder_size"] = 0.0
        content = folder_data(folder_path)
        return {"content": content, "total_size": globals()["folder_size"]}
    else:
        return {}


def search_file(name, data):
    for i in data["files"]:
        if i["filename"] == name:
            return {"filename": name, "path": join(".", data["path"], name) if "path" in data else f"./{name}"}
    for folder in data["folders"]:
        for i in folder["files"]:
            if i["filename"] == name:
                return {"filename": name, "path": join(".", folder["path"], name) if "path" in folder else f"./{name}"}
        for i in folder["folders"]:
            search_file(name, i)
    return {}


def get_json(folder, filename):
    folder_path = folder if folder.startswith("./") else f"./{folder}"
    if isdir(folder_path):
        file_path = join(
            folder_path,
            filename if filename.endswith(".json") else f"{filename}.json"
        )
        if isfile(file_path):
            return load(open(file_path))
    else:
        return {}


def save_json(folder, filename, data):
    folder_path = folder if folder.startswith("./") else f"./{folder}"
    if isdir(folder_path):
        file_path = join(
            folder_path,
            filename if filename.endswith(".json") else f"{filename}.json"
        )
        with open(file_path, "w") as f:
            f.write(dumps(
                data,
                indent=4, sort_keys=True, ensure_ascii=False
            ))
            f.close()
    return


def save_file(folder, filename, data, extension=None):
    folder_path = folder if folder.startswith("./") else f"./{folder}"
    if isdir(folder_path):
        file_path = join(
            folder_path,
            f"{filename}.{extension}" if extension else filename
        )
        with open(file_path, "w") as f:
            f.write(data)
            f.close()
    return


def create_zip(folder_path):
    if isdir(folder_path):
        zip_path = folder_path + ".zip"
        with ZipFile(zip_path, 'w') as zipObj:
            for folderName, subfolders, filenames in walk(folder_path):
                for filename in filenames:
                    filePath = join(folderName, filename)
                    zipObj.write(filePath)
        return {"filename": zip_path.split("/")[-1], "path": zip_path}
    else:
        return {"response": "folder not found"}


def remove_zip(zip_path):
    remove(zip_path)
    return


def get_info_zip(zip_path):
    name = zip_path.split('/')[-1]
    folder_path = zip_path.replace(f"/{name}", "")
    data = []
    str_data = getoutput(f"cd {folder_path} && python -m zipfile -l ./{name}").splitlines()[1:]
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

