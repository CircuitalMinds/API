import os
import json
from string import ascii_lowercase
from bs4 import BeautifulSoup
import requests


class VideoContainers:

    class Container:

        def __init__(self, path, id):
            self.path = path
            self.__name__ = id
            self.data = json.load(open(f'{path}/info.json'))
            self.meta_data = {
                name.replace('.html', ''): open(
                    f'{path}/meta_data/{name}').read() for name in os.listdir(f'{path}/meta_data')
            }

        @property
        def video_list(self):
            return self.data['video_list']

        @property
        def available_space(self):
            return self.data['available_space']

        @property
        def container_size(self):
            return self.data['container_size']

    def __init__(self, path):
        self.path = path
        self.git_url = 'https://github.com/circuitalmynds'
        self.ids = [ly for ly in ascii_lowercase]
        self.size_limits = dict(size_max=50.0, total_size=980.0)
        self.set_containers()

    def set_containers(self):
        for id in self.ids:
            self.__setattr__(
                id, self.Container(path=f'{self.path}/music_{id}', id=id)
            )

    def get_video_urls(self, id):
        get_response = requests.get(f'{self.git_url}/music_{id}/tree/main/videos').text
        targets = {"name": 'a', "class": 'js-navigation-open Link--primary'}
        urls = BeautifulSoup(get_response, 'html.parser').find_all(**targets)
        return {a.get('title'): f'https://github.com{a.get("href")}?raw=true' for a in urls}

    def get_data_from(self, container, attribute_name, return_list=True):
        if return_list:
            return [{k: v} for k, v in self.__dict__[container].__dict__[attribute_name].items()]
        else:
            return self.__dict__[container].__dict__[attribute_name]

    def get_containers_data(self):
        factor = 1024.0 ** 2
        for id in self.ids:
            data = dict(
                total_size=0.0, size_max=0.0, size_min=0.0, size_mean=0.0,
                video_list=self.get_video_urls(id=id), file_sizes=dict(), available_space=True
            )
            from_path = f'{self.path}/music_{id}'
            for video in os.listdir(f'{self.path}/music_{id}/videos'):
                video_path = f'{from_path}/videos/{video}'
                data['file_sizes'][video] = float(os.stat(video_path).st_size / factor)
            sizes = list(data['file_sizes'].values())
            data['total_size'] = sum(sizes)
            data['size_max'] = max(sizes)
            data['size_min'] = min(sizes)
            data['size_mean'] = data['total_size'] / len(sizes)
            if data['total_size'] > self.size_limits['total_size']:
                data['available_space'] = False
            with open(f'{self.path}/music_{id}/info.json', 'w') as outfile:
                json_file = json.dumps(data, indent=4, sort_keys=True)
                outfile.write(json_file)
                outfile.close()

    def check_restrictions(self):
        size_data = {}
        for name in size_data.keys():
            data = size_data[name]
            check_data = (
                data[key] > self.size_limits[key] for key in ['size_max', 'total_size']
            )
            if any(check_data):
                print(f'Warning. Container with id: {name} is full. {data["size_max"]}, {data["total_size"]}')

    def git_push(self):
        for id in self.ids:
            go_to = f"cd {self.path}/music_{id}"
            push = "git push"
            command = f'{go_to} && {push}'
            print(command)
            os.system(command=command)


Id = 'wgl01LTmYKc'
Title = 'Joaquin Sabina - Y Nos Dieron las Diez'
yt_search = lambda Title: f'https://www.youtube.com/results?search_query={Title}'
yt_watch = lambda Id: f'https://www.youtube.com/watch?v={Id}'

#get_data = requests.get(yt_watch(Id=Id)).text
get_data = requests.get(yt_search(Title=Title)).text
s = BeautifulSoup(get_data, 'html.parser')
string_data = s.find('body').prettify().split('"videoId":"')
data = []
for r in string_data:
    y = r.split('"')[0]
    if len(y) == 11 and y not in data:
        data.append(y)
print(data)