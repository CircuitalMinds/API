import json
import requests
import os


path = "../../../music_containers"
get_url = lambda container, song: f"/{container}/{requests.utils.quote(song)}"
git_commit = lambda: os.system("cd .. && git init && git add . && git commit -m 'auto'")
git_push = lambda: os.system("cd .. && git push")
data_containers = ["music_container"]
data_containers.extend([f"music_container_{j}" for j in range(1, 18)])
header = [{"name": "id", "title": "ID", "size": 50, "sortable": "true", "sortDir": "asc", "format": "number"},
          {"name": "name", "title": "Name", "sortable": "true"}]


def save_data(data_files):
    for name in data_files:
        with open(f"{name}.json", "w") as outfile:
            json_file = json.dumps(data_files[name], indent=4, sort_keys=True)
            outfile.write(json_file)
            outfile.close()


def get_data_from(containers):
    data = {}
    for container in containers:
        songs = os.listdir(f"{path}/{container}/videos")
        meta = json.load(open(f"{path}/{container}/meta_tags.json"))
        for song_id in meta:
            ids = [s.find(song_id) != -1 for s in songs]
            if True in ids:
                song = songs[ids.index(True)]
                data[song_id] = meta[song_id]
                data[song_id]["url_content"] = get_url(container=container, song=song)
    return data


def build_data_list(data):
    set_data = lambda song: {"video_title": song["video_title"],
                             "video_url": song["url_content"]}
    return {"data_list": [set_data(song=data[i]) for i in data]}


def build_template_list(data_list):
    template = ['<button style="border: 1px solid dark; margin: 0; width: 100%; height: 100%;" class="button fg-teal" ',
                'onclick="Player.play_from_list(INDEX);">TITLE</button>']
    row = lambda index, title: template[0] + template[1].replace("INDEX", str(index)).replace("TITLE", title)
    rows = []
    for i in range(len(data_list)):
        rows.append([i + 1, row(index=i, title=data_list[i]["video_title"])])
    return {"header": header, "data": rows}


data = get_data_from(data_containers)
data_list = build_data_list(data=data)
template_list = build_template_list(data_list=data_list['data_list'])
meta_tags = {s: {attr: data[s][attr]
                 for attr in ["http-equiv", "name", "property", "itemprop"]} for s in data}
save_data(data_files=dict(data_list=data_list, template_list=template_list, meta_tags=meta_tags))

