import requests
import os
import json
from string import ascii_lowercase
from bs4 import BeautifulSoup


class Container:

    def __init__(self, path, name):
        self.__name__ = name
        self.path = path
        self.video_list = json.load(open(f'{path}/video_list.json'))['video_list']
        self.meta_data = {
            name.replace('.html', ''): open(
                f'{path}/meta_data/{name}').read() for name in os.listdir(f'{path}/meta_data')
        }
        self.search_data = dict()

    def save_search_data(self):
        with open(f"{self.path}/meta_data/wiki_search.json", "w") as outfile:
            json_file = json.dumps(self.search_data, indent=4, sort_keys=True)
            outfile.write(json_file)
            outfile.close()


class VideoContainers:
    path = '../music_containers'

    def set_containers(self):
        for ly in ascii_lowercase:
            dir_path = f'{self.path}/music_{ly}'
            self.__setattr__(ly, Container(path=dir_path, name=ly))
    
    def get_data_from(self, container, attribute_name, return_list=True):
        if return_list:
            return [{k: v} for k, v in self.__dict__[container].__dict__[attribute_name].items()]
        else:
            return self.__dict__[container].__dict__[attribute_name]


class Wikipedia:

    wiki = 'https://en.wikipedia.org/wiki'

    def query_video_by_title(self, title):
        data = dict()
        title = title.split()
        search = '_'.join(title[:title.index('-')]) if '-' in title else '_'.join(title)
        response = requests.get(f'{self.wiki}/{search}').text
        try:
            html_parser = BeautifulSoup(response, 'html.parser').find('table').find_all('tr')
            for tr in html_parser:
                if tr.find('th') is not None and tr.find('td') is not None:
                    content = list(dict.fromkeys(tr.find('td').text.split('\n')).keys())
                    if '' in content:
                        content.remove('')
                    if len(content) == 1:
                        data[tr.find('th').text] = content[0]
                    else:
                        data[tr.find('th').text] = content
        except AttributeError:
            pass
        return data


def get_wiki_data():
    video_containers = VideoContainers()
    video_containers.set_containers()
    wiki = Wikipedia()
    for name in ascii_lowercase:
        video_container = video_containers.__dict__[name]
        for title in video_container.video_list.keys():
            video_container.search_data[title] = wiki.query_video_by_title(title=title)
        video_container.save_search_data()


get_wiki_data()
