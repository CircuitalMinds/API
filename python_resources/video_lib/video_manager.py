import os
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
        self.video_storages = {}

    def set_containers(self):
        set_data = lambda path: {"path": path, "files": os.listdir(path)}
        self.video_storages.update({
            "waiting_files": set_data(f"{self.path}/waiting_files"),
            "trash_files": set_data(f"{self.path}/trash_files"),
            "rejected_files": set_data(f"{self.path}/rejected_files")
        })
        sections = [f'{self.path}/section_{i}' for i in range(2)]
        for section in sections:
            for container_name in os.listdir(section):
                container_id = container_name.split('_')[-1]
                self.ids.append(container_id)
                container_path = f"{section}/{container_name}"
                self.__dict__[container_id] = {
                    "path": container_path,
                    "videos": set_data(f"{container_path}/videos"),
                    "wikidata": set_data(f"{container_path}/wikidata"),
                    "metadata": set_data(f"{container_path}/metadata")
                }

    def get_container_data(self, container_id):
        data = {"info_container": self.get_file_sizes(container_id), "video_data": {}}
        key_list = [
            'title', 'og:image', 'description', 'keywords', 'duration', 'interactionCount'
        ]
        metadata = self.get_metadata(container_id=container_id)
        url_data = self.get_url_data(container_id=container_id)
        is_id = lambda data_id: list(
            filter(lambda title: title.replace('.mp4', '')[-11:] == data_id, list(url_data))
        )
        for name in list(metadata):
            meta = metadata[name]
            if "videoId" in list(meta):
                video_id = meta["videoId"]
                is_video_id = is_id(video_id)
                if is_video_id:
                    video_name = is_video_id[0]
                    data['video_data'][video_name] = {"video_id": video_id, "url": url_data[video_name]}
                    for key in key_list:
                        if key in list(meta):
                            value = meta[key]
                            if key == 'og:image':
                                key = key.replace('og:', '')
                            if key == 'interactionCount':
                                key = key.replace('Count', '_count')
                            if key == 'duration':
                                value = value.replace('PT', '').replace('M', ':').replace('S', '')
                            data['video_data'][video_name][key] = value
        return data

    def get_url_data(self, container_id):
        video_urls = {}
        get_data = requests.get(f'{self.git_url}/music_{container_id}/tree/main/videos').text
        targets = {"name": 'a', "class": 'js-navigation-open Link--primary'}
        urls = Analyzer(get_data, 'html.parser').find_all(**targets)
        for url in urls:
            title = url.get("title")
            video_urls[title] = f'https://github.com{url.get("href")}?raw=true'
        return video_urls

    def get_metadata(self, container_id):
        data = {}
        metadata = self.__dict__[container_id]['metadata']
        metadata_path = metadata['path']
        metadata_files = metadata['files']
        for filename in metadata_files:
            data[filename] = {}
            video_data = Analyzer(
                open(os.path.join(metadata_path, filename)).read(), 'html.parser'
            ).find_all('meta')
            for meta in video_data:
                attrs, meta_name, meta_content = meta.__dict__['attrs'], "", ""
                if 'content' in list(attrs):
                    for name in list(attrs):
                        if name == 'content':
                            meta_content += attrs[name]
                        else:
                            meta_name += attrs[name]
                    data[filename][meta_name] = meta_content
        return data

    def get_file_sizes(self, container_id):
        factor = 1024.0 ** 2
        sizes = []
        videos_path = self.__dict__[container_id]['videos']['path']
        for title in os.listdir(videos_path):
            sizes.append(
                float(os.stat(f'{videos_path}/{title}').st_size / factor)
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
            id=container_id,
            total_size=total_size,
            size_max=size_max,
            size_min=size_min,
            size_mean=size_mean,
            available_space=available_space
        )
        return data

    def check_restrictions(self, container_id):
        size_data = self.get_file_sizes(container_id)
        print(f'{container_id}: {size_data}')
        check_data = (
            size_data[key] > value for [key, value] in self.size_limits.items()
        )
        if any(check_data):
            print(
                f'''Warning. Container music_{container_id} is already full. 
                                    {size_data["size_max"]}, {size_data["total_size"]}'''
            )
            return 'failed'
        else:
            return 'success'

