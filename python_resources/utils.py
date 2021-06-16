def save_object_file(path, data, filetype):
    if filetype == 'yaml':
        import yaml
        with open(path, "w") as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
    else:
        import json
        with open(path, 'w') as outfile:
            json_file = json.dumps(data, indent=4, sort_keys=True)
            outfile.write(json_file)
            outfile.close()


def open_object_file(path):
    filetype = path.split('.')[1]
    if filetype == 'yml':
        import yaml
        return yaml.load(open(path), Loader=yaml.FullLoader)
    else:
        import json
        return json.load(open(path))


def get_info_resources(path, lib_names=None, save_file=False):
    if save_file and lib_names is not None:
        import os
        check_data = lambda filename: filename not in ['__init__.py', '__pycache__']
        replace = lambda filename: filename.replace('.py', '')
        libs = dict()
        for lib_name in lib_names:
            lib_path = f'./python_resources/{lib_name}'
            libs[lib_name] = dict(modules=[])
            for module in os.listdir(lib_path):
                if check_data(filename=module):
                    libs[lib_name]['modules'].append(replace(filename=module))
        save_object_file(path=path, data=dict(libs=libs), filetype='json')
    else:
        return open_object_file(path=path)


class SystemProcess:

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
