import requests
import os
from bs4 import BeautifulSoup as Analyzer
yt_url = "https://www.youtube.com"


def search(video_title):
    return Analyzer(
        requests.get(f"{yt_url}/results?search_query={video_title}").text, 'html.parser'
    )


def watch(video_id):
    return Analyzer(
        requests.get(f"{yt_url}/watch?v={video_id}").text, 'html.parser'
    )


def get_video_ids(video_title):
    strings = search(video_title=video_title).find('body').prettify().split('"videoId":"')
    ids = []
    for string in strings:
        video_id = string.split('"')[0]
        if all([len(video_id) == 11, video_id not in ids]):
            ids.append(video_id)
    return dict(video_ids=ids)


def get_video_metadata(video_id):
    parsed = watch(video_id=video_id)
    title = parsed.find('title').__str__()
    document = [
        '<!DOCTYPE html>', '<html lang="en">', '<head>',
        '<meta charset="UTF-8">', title
    ]
    for meta in parsed.find('head').find_all('meta'):
        document.append(meta.__str__())
    document.extend([
        '</head>', '<body>', '</body>', '</html>'
    ])
    return dict(
        metadata=Analyzer('\n'.join(document), 'html.parser').prettify()
    )


def downloader(video, downloads_path='./'):
    command = ''
    if "title" in list(video):
        command += f'cd {downloads_path} && youtube-dl -f mp4 "ytsearch:{video["title"]}"'
    elif "id" in list(video):
        command += f'cd {downloads_path} && youtube-dl -f mp4 {yt_url}/watch?v={video["id"]}'
    if command != '':
        print(os.system(command))
    else:
        pass
