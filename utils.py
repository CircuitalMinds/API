class System:

    current_directory = {"files": {}, "directories": {}}

    def goto(self, path):
        from subprocess import getoutput
        import os
        self.current_directory = {"files": {}, "directories": {}}
        commands = " && ".join([
            f"cd {path}", "ls"
        ])
        add_data = lambda dir_path: self.current_directory["files"].update({
            dir_path.split("/")[-1]: dir_path
        }) if os.path.isfile(dir_path) else self.current_directory["directories"].update({
            dir_path.split("/")[-1]: dir_path
        })
        for name in getoutput(commands).splitlines():
            add_data(dir_path=os.path.join(path, name))


class FileHandlers:

    directories = {}
    files = {}
    parsed_documents = {}


    def file_size(self, file_path):
        from os import stat
        return float(stat(file_path).st_size * 1024 ** -2)

    @staticmethod
    def size_dir(path, size_unit="MB"):
        from os import stat, listdir
        factor = 1.0
        size_data = dict()
        if size_unit == 'MB':
            factor = 1024.0 ** 2
        get_size = lambda filename: float(stat(f'{path}/{filename}').st_size / factor)
        for filename in listdir(path):
            size_data[filename] = get_size(filename=filename)
        return size_data

    @staticmethod
    def date_dir(dir_path):
        from time import localtime
        from os import stat, path
        if path.isdir(dir_path) or path.isfile(dir_path):
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
        from os import rename, path
        check_paths = all(
            any([path.isdir(name), path.isfile(name)]) for name in [from_path, to_path]
        )
        if check_paths:
            rename(from_path, to_path)
        else:
            pass

    @staticmethod
    def create_directory(to_path):
        from os import path, mkdir
        if path.isdir(to_path) is False:
            mkdir(to_path)
        else:
            pass

    def save_file(self, path, data):
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

    def open_file(self, path):
        filetype = path.endswith
        if filetype('yml'):
            import yaml
            return yaml.load(open(path), Loader=yaml.FullLoader)
        elif filetype('json'):
            import json
            return json.load(open(path))
        else:
            return open(path).read()

    def html_parser(self, file, target):
        from bs4 import BeautifulSoup as Analyzer
        parsed = Analyzer(file, 'html.parser')
        data = {}
        data[target] = parsed.find_all(target)
        return data

    def directory_tree(self, path, by_filter=None):
        from subprocess import getoutput
        from yaml import load, FullLoader
        out = getoutput(f'cd {path} && tree -J')
        outfile = load(out, Loader=FullLoader)[0]['contents']
        if by_filter is None:
            return outfile
        else:
            return list(filter(lambda file_i: "contents" in list(file_i), outfile))


class ObjectIterators:

    def object_iterator(self, data):
        return list(map(lambda key: data[key], data))

    def object_filter(self, data, filter_function):
        return {i: data[i] for i in list(
            filter(filter_function, data)
        )}
