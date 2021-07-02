from os import listdir, stat
import requests
from . import video, container, youtube

Analyzer = youtube.Analyzer


class VideoManager:
    container = container.Container
    container.video = video.Video

    def __init__(self, path):
        self.path = path
        self.git_url = 'https://github.com/circuitalmynds'
        self.ids = []
        self.size_limits = dict(size_max=50.0, total_size=980.0)
        self.downloads_path = './python_resources/video_lib/downloads'
        self.data_search = {}
        self.containers_data = {}

    def set_containers(self):
        from subprocess import getoutput
        import os
        data = {"files": {}, "directories": {}}
        get_data = lambda path: [
            data["directories"].update({
                dir_path: f"{path}/{dir_path}"
            }) if dir_path.split(".")[-1] == dir_path else data["files"].update({
                dir_path: f"{path}/{dir_path}"
            }) for dir_path in getoutput(f"cd {path} && ls").splitlines()
        ]
        for d in os.listdir(self.path):
            if os.path.isdir(f"{self.path}/{d}"):
                get_data(f"{self.path}/{d}")
            else:
                data["files"].update({d: f"{self.path}/{d}"})
        self.containers_data = data
        self.ids.extend([
            data_id.split("_")[-1] for data_id in list(self.containers_data["directories"])
        ])
        for id in self.ids:
            self.__dict__[id] = self.containers_data["directories"][f"music_{id}"]

    def update_container_data(self, container_id=None):
        iter_data = self.ids if container_id is None else [container_id]
        for id in iter_data:
            info = dict(
                info_container=self.get_file_sizes(id=id),
                video_list=self.get_video_list(id=id)
            )
            info['info_container'] = self.get_file_sizes(id=id)
            info['video_list'] = self.get_video_list(id=id)
            for filename, data in info.items():
                return dict(
                    data=data,
                    filename=f'music_{id}/{filename}',
                    filetype='json'
                )

    def get_video_list(self, id):
        get_response = requests.get(f'{self.git_url}/music_{id}/tree/main/videos').text
        targets = {"name": 'a', "class": 'js-navigation-open Link--primary'}
        urls = Analyzer(get_response, 'html.parser').find_all(**targets)

        def get_image(title):
            video_id = title.split('-')[-1].split('.mp4')[0]
            if len(video_id) == 11:
                return f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'
            else:
                return 'https://circuitalminds.github.io/static/images/desktop/julia.gif'
        return {a.get('title'): {
            'url': f'https://github.com{a.get("href")}?raw=true',
            'image': get_image(title=a.get('title'))} for a in urls
        }

    def get_file_sizes(self, id):
        factor = 1024.0 ** 2
        sizes = []
        to_path = self.__dict__[id]
        for title in listdir(f'{to_path}/videos'):
            sizes.append(
                float(stat(f'{to_path}/videos/{title}').st_size / factor)
            )
        if len(sizes) == 0:
            sizes.append(0)
        total_size = sum(sizes)
        size_max = max(sizes)
        size_min = min(sizes)
        size_mean = total_size / len(sizes)
        available_space = True
        if total_size > self.size_limits['total_size']:
            available_space = False
        data = dict(
            id=id,
            total_size=total_size,
            size_max=size_max,
            size_min=size_min,
            size_mean=size_mean,
            available_space=available_space
        )
        return data

    def check_restrictions(self, check_id=None):
        if check_id is None:
            for id in self.ids:
                size_data = self.get_file_sizes(id=id)
                print(f'{id}: {size_data}')
                check_data = (
                    size_data[key] > value for [key, value] in self.size_limits.items()
                )
                if any(check_data):
                    print(
                        f'''Warning. Container music_{id} is already full. 
                        {size_data["size_max"]}, {size_data["total_size"]}'''
                    )
        else:
            size_data = self.get_file_sizes(id=check_id)
            check_data = (
                size_data[key] > value for [key, value] in self.size_limits.items()
            )
            if any(check_data):
                return 'failed'
            else:
                return 'success'

