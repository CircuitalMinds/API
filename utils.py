from os import remove, walk
from os.path import join, isdir, isfile
from zipfile import ZipFile
from json import load, dumps
from yaml import full_load
from subprocess import getoutput


class Dumper:
    json = dict(
        indent=4, sort_keys=True, ensure_ascii=False
    )
    yml = dict(
        allow_unicode=False, indent=4, default_flow_style=False
    )

    @staticmethod
    def write_file(file_path, data):
        with open(file_path, "w") as f:
            f.write(data)
            f.close()
        return

    @staticmethod
    def open_file(file_path):
        if isfile(file_path):
            return open(file_path)
        else:
            return None

    @classmethod
    def open_json(cls, json_file, *keys):
        data = cls.open_file(json_file)
        if data:
            json_data = load(data)
            if keys:
                return cls.get_values(json_data, keys)
            else:
                return json_data
        else:
            return {}

    @classmethod
    def open_yaml(cls, yaml_file, *keys):
        data = cls.open_file(yaml_file)
        if data:
            yaml_data = full_load(data)
            if keys:
                return cls.get_values(yaml_data, keys)
            else:
                return yaml_data
        else:
            return {}

    @classmethod
    def write_json(cls, file_path, data):
        cls.write_file(file_path, data=dumps(data, **cls.json))
        return

    @classmethod
    def write_yaml(cls, file_path, data):
        import yaml
        cls.write_file(*file_path, data=yaml.dump(data, **cls.yml))
        return

    @staticmethod
    def get_values(data, keys):
        return {
            key: data[key]
            for key in keys if key in data
        }


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
