def join_path(path_a, path_b):
    import os
    return os.path.join(path_a, path_b)


def is_file(file_path):
    import os
    return os.path.isfile(file_path)


def is_dir(dir_path):
    import os
    return os.path.isdir(dir_path)


class SystemBrowser:

    @staticmethod
    def goto(path):
        from subprocess import getoutput
        current_directory = {"files": {}, "directories": {}}
        commands = " && ".join([
            f"cd {path}", "ls"
        ])
        add_data = lambda dir_path: current_directory["files"].update({
            dir_path.split("/")[-1]: dir_path
        }) if is_file(dir_path) else current_directory["directories"].update({
            dir_path.split("/")[-1]: dir_path
        })
        for name in getoutput(commands).splitlines():
            add_data(dir_path=join_path(path, name))
        return current_directory


class FileHandlers:
    allowed_files = {
        "documents": ["pdf", "txt", "md", "html", "json", "yml"],
        "media": ["psd", "woff", "svg", "ttf", "ico", "png", "jpeg", "jpg", "gif", "mp4", "mp3"],
        "scripts": ["py", "js", "css", "ipynb", "php", "map", "less", "sqlite3"]
    }
    ignored_files = ["environment", ".git", "__pycache__", ".idea"]

    @staticmethod
    def file_size(file_path):
        from os import stat
        return float(stat(file_path).st_size * 1024 ** -2)

    @staticmethod
    def size_dir(path, size_unit="MB"):
        from os import stat, listdir
        factor = 1.0
        size_data = dict()
        if size_unit == 'MB':
            factor = 1024.0 ** 2
        get_size = lambda filename: float(stat(join_path(path, filename)).st_size / factor)
        for filename in listdir(path):
            size_data[filename] = get_size(filename=filename)
        return size_data

    @staticmethod
    def date_dir(dir_path):
        from time import localtime
        from os import stat
        if is_dir(dir_path) or is_file(dir_path):
            data = localtime(stat(dir_path).st_atime)
            return {
                'day': data.tm_mday,
                'month':  data.tm_mon,
                'year':  data.tm_year,
                'time': f'{data.tm_hour}:{data.tm_min}:{data.tm_sec}'
             }
        else:
            pass

    @staticmethod
    def move_file(from_path, to_path):
        from os import rename
        check_paths = all(
            any([is_dir(name), is_file(name)]) for name in [from_path, to_path]
        )
        if check_paths:
            rename(from_path, to_path)
        else:
            pass

    @staticmethod
    def create_directory(to_path):
        from os import path, mkdir
        if is_dir(to_path) is False:
            mkdir(to_path)
        else:
            pass

    @staticmethod
    def save_file(path, data):
        filetype = path.endswith
        if filetype('yaml'):
            import yaml
            with open(path, "w") as outfile:
                yaml.dump(data, outfile, default_flow_style=False)
        elif filetype('json'):
            import json
            with open(path, 'w') as outfile:
                json_file = json.dumps(data, indent=4, sort_keys=True)
                outfile.write(json_file)
                outfile.close()
        else:
            with open(path, 'w') as outfile:
                outfile.write(data)
                outfile.close()

    @staticmethod
    def open_file(path):
        filetype = path.endswith
        if filetype('yml'):
            import yaml
            return yaml.load(open(path), Loader=yaml.FullLoader)
        elif filetype('json'):
            import json
            return json.load(open(path))
        else:
            return open(path).read()

    @staticmethod
    def html_parser(file, target):
        from bs4 import BeautifulSoup as Analyzer
        parsed = Analyzer(file, 'html.parser')
        data = {}
        data[target] = {}
        for tag in parsed.find_all(target):
            print(tag.__dict__["attrs"])

        return data

    @staticmethod
    def directory_tree(path, by_filter=None):
        from subprocess import getoutput
        from yaml import load, FullLoader
        out = getoutput(f'cd {path} && tree -J')
        outfile = load(out, Loader=FullLoader)[0]['contents']
        if by_filter is None:
            return outfile
        else:
            return list(filter(lambda file_i: "contents" in list(file_i), outfile))


class Iterators:

    @staticmethod
    def filter_data(data, key_list):
        filtered = {}
        lower = lambda key_data: key_data.lower()
        check_attr = lambda name, target: name in target or target in name
        for key in key_list:
            filtered[key] = {
                attr: data[attr] for attr in list(
                    filter(lambda name: check_attr(name=lower(name), target=lower(key)), list(data))
                )
            }
        return filtered

    @staticmethod
    def object_iterator(data):
        return list(map(lambda key: data[key], data))

    @staticmethod
    def object_filter(data, filter_function):
        return {i: data[i] for i in list(
            filter(filter_function, data)
        )}
