import os
from utils import FileHandlers
from video_lib import video_manager, Container, Finders


def get_repositories():
    from bs4 import BeautifulSoup as Analyzer
    import requests
    info_data = FileHandlers.open_file(path='info.json')
    git = 'https://github.com'
    organization = 'CircuitalMinds'
    request_data = Analyzer(requests.get(f'{git}/{organization}').text, 'html.parser')
    repos = request_data.find_all('a', {'itemprop': 'name codeRepository'})
    data = dict(repositories={
        link.text.split()[0]: git + link.get("href") for link in repos
    })
    info_data.update(data)
    FileHandlers.save_file(path='info.json', data=info_data)
    return info_data


def get_storage_info():
    path = './storage'
    join = lambda fpath: os.path.join(path, os.path.join(*fpath))
    is_file = os.path.isfile
    join = os.path.join
    get_dirs = lambda fpath: {
        f: join([fpath, f]) if is_file(join([fpath, f])) else {
            d: join([fpath, f, d]) for d in os.listdir(join([fpath, f]))
        } for f in os.listdir(join([fpath]))
    }
    directory_data = {d: get_dirs(d) for d in os.listdir(path)}
    info_data = FileHandlers.open_file(path='info.json')
    info_data.update({"storage_data": directory_data})
    FileHandlers.save_file(path='info.json', data=info_data)
