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


def html_parser(file, target):
    from bs4 import BeautifulSoup as Analyzer
    parsed = Analyzer(file, 'html.parser')
    data = {}
    data[target] = parsed.find_all(target)
    return data


def directory_tree(path, by_filter=None):
    from subprocess import getoutput
    from yaml import load, FullLoader
    out = getoutput(f'cd {path} && tree -J')
    outfile = load(out, Loader=FullLoader)[0]['contents']
    if by_filter is None:
        return outfile
    else:
        return list(filter(lambda file_i: "contents" in list(file_i), outfile))


def object_iterator(data):
    return list(map(lambda key: data[key], data))


def object_filter(data, filter_function):
    return {i: data[i] for i in list(
        filter(filter_function, data)
    )}


def filetype_filter(filename, filetype):
    is_filetype = filename.lower().split('.')[-1].endswith
    return is_filetype(filetype)

def directory_filter(path, only_files=True):
    import os
    by_check = os.path.isfile if only_files else os.path.isdir
    if by_check(path):
        return True
    else:
        return False


def move_file(filename, from_path, to_path):
    from os import rename, path
    in_path, out_path = ['/'.join([path_i, filename]) for path_i in [from_path, to_path]]
    is_filename = path.isfile
    if all([is_filename(in_path) is True, is_filename(out_path) is False]):
        #rename(in_path, out_path)
        print(in_path, out_path)
    else:
        pass


def goto(path, from_data=None, get_data=None):
    from subprocess import getoutput
    import os
    commands = " && ".join([
        f"cd {path}", "ls"
    ])
    data_list = {"files": {}, "directories": {}}
    add_data = lambda dir_path: data_list["files"].update({
        dir_path.split("/")[-1]: dir_path
    }) if os.path.isfile(dir_path) else data_list["directories"].update({
        dir_path.split("/")[-1]: dir_path
    })
    for name in getoutput(commands).splitlines():
        add_data(dir_path=os.path.join(path, name))
    if from_data is None:
        return data_list
    elif from_data in list(data_list):
        send_data = data_list[from_data]
        if get_data is None:
            return send_data
        elif get_data in list(send_data):
            return send_data[get_data]
        else:
            return send_data
    else:
        return data_list


def checking(x, y):
    """
    for i, j in range(n):

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    x_list, y_list = word_tokenize(x), word_tokenize(y)
    sw = stopwords.words('english')
    l1, l2 = [], []
    x_set = {w for w in x_list if w not in sw}
    y_set = {w for w in y_list if w not in sw}
    r_vector = x_set.union(y_set)
    c = 0
    add_element = lambda element, to_add, into_set: to_add.append(1) if element in into_set else to_add.append(0)
    for w in r_vector:
        if w in x_set:
            add_element(element=w, to_add=l1, into_set=x_set)
        if w in y_set:
            add_element(element=w, to_add=l2, into_set=y_set)
    n = sum(l1) * sum(l2)
    if n != 0:
        for i in range(len(r_vector)):
            c += l1[i] * l2[i]
        return c / (float(n) ** 0.5)
    else:
        return 0.0
    """


class FileSystem:

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


class Containers:

    data = dict()
    path = '../music_containers'
    restrictions = dict(
        size_max=50.0, total_size=980.0
    )

    def get_data(self):
        import os
        for section in os.listdir(self.path):
            section_path = f'{self.path}/{section}'
            if section == 'rejected_files':
                self.data[section] = {
                    "files": os.listdir(section_path),
                    "path": section_path
                }
            else:
                for name in os.listdir(section_path):
                    self.data[name.split('_')[-1]] = {
                        'path': f'{section_path}/{name}',
                        'info_container': open_file(f'{section_path}/{name}/info_container.json'),
                        'video_list': open_file(f'{section_path}/{name}/video_list.json')
                    }
        return self.data

    def update_info(self):
        container_ids = list(self.data.keys())
        container_ids.remove('rejected_files')
        for container_id in container_ids:
            info = self.container_data(container_id=container_id)
            for name in info.keys():
                save_file(path=f'{self.data[container_id]["path"]}/{name}', data=info[name])

    def file_size(self, file_path):
        from os import stat
        return float(stat(file_path).st_size * 1024 ** -2)

    def container_data(self, container_id):
        import os
        from bs4 import BeautifulSoup
        container_path = self.data[container_id]["path"]
        sizes = []
        video_list = dict()

        def set_video_data(filename):
            html_file = f'{container_path}/metadata/{filename.replace("mp4", "html")}'
            default = dict(
                title=filename.replace('.mp4', ''),
                image='https://circuitalminds.github.io/static/images/desktop/julia.gif',
                url=f'{container_path}/videos/{filename}'
            )
            if f'-{filename.replace(".mp4", "")[-11:]}' in filename.replace(".mp4", ""):
                video_id = filename.replace(".mp4", "")[-11:]
                title = filename.replace(".mp4", "")[:-12]
                return dict(
                    title=title,
                    image=f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg',
                    url=f'{container_path}/videos/{filename}'
                )
            elif os.path.isfile(html_file):
                html = BeautifulSoup(open(html_file).read(), 'html.parser')
                metadata = lambda data: html.find("meta", data)
                video_id = metadata(data=dict(itemprop="videoId"))
                title = metadata(data=dict(name="title"))
                if video_id is not None and title is not None:
                    return dict(
                        title=title.get('content'),
                        image=f'https://i.ytimg.com/vi/{video_id.get("content")}/hqdefault.jpg',
                        url=f'{container_path}/videos/{filename}'
                    )
            else:
               return default

        for filename in os.listdir(f'{container_path}/videos'):
            video_list[filename] = set_video_data(filename=filename)
            sizes.append(self.file_size(file_path=f'{container_path}/videos/{filename}'))
        if len(sizes) == 0:
            sizes.append(0.0)
        total_size = sum(sizes)
        size_min, size_max, size_mean = min(sizes), max(sizes), total_size / len(sizes)
        available_space = True if all(
                [size_max < self.restrictions['size_max'], total_size < self.restrictions['total_size']]
        ) else False
        info_container = dict(
            id=container_id, total_size=total_size, available_space=available_space,
            size_max=size_max, size_min=size_min, size_mean=size_mean
        )
        return dict(video_list=video_list, info_container=info_container)

    def move_to_rejected_files(self, in_path):
        filename = in_path.split('/')[-1]
        out_path = f'{self.data["rejected_files"]["path"]}/{filename}'
        print(in_path, out_path)

    def move_files_to_container(self, container_id, file_path):
        import os
        if os.path.isfile(file_path):
            if self.file_size(file_path=file_path) < self.restrictions["size_max"]:
                filename = file_path.split('/')[-1]
                print(file_path, f'{self.data[container_id]["path"]}/videos/{filename}')
            else:
                self.move_to_rejected_files(in_path=file_path)
        else:
            pass
