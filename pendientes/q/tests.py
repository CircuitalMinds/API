
def test_meta_tags():
    conts = [f"../../music_containers/pendientes/music_{j}"
             for j in range(1, 8)]
    for n in range(len(conts)):
        data = {}
        dir_path = f"{path}/music_container_{n + 11}"
        data_list = os.listdir(f"{dir_path}/videos")
        data_test = [song.replace(".mp4", "")[::-1][:11][::-1] for song in data_list]
        music_data = json.load(open(f"{conts[n]}/music_data.json"))
        for song in music_data:
            if song in data_test:
                data[song] = music_data[song]
        save_data(data, f"{dir_path}/meta_tags")

def test_data(n):
    containers = [data_containers[n]]
    data = get_data_from(containers=containers)
    song_list = list(data.keys())
    meta = json.load(open("./music_meta_tags_list.json"))
    new_data = {}
    for m in meta.values():
        k = list(m.keys())
        if k:
            test = [s.replace(".mp4", "")[::-1][:11][::-1] in k for s in song_list]
            if any(test):
                new_data[k[0]] = m[k[0]]
            elif k[0] in [s.replace(".mp4", "")[::-1][:11][::-1] for s in song_list]:
                new_data[k[0]] = m[k[0]]
    save_data(data=new_data, file_name=f"{path}/{containers[0]}/meta_tags")



def get_meta_data(data):
    api = "http://127.0.0.1:5000/api/get_youtube_search_song"
    #meta_data = json.load(open("./music_meta_tags_list.json"))
    meta_data = {}
    for s in range(len(data)):
        video_title = data[s]["video_title"]
        video_url = data[s]["video_url"]
        meta_data.update({video_title: requests.get(api, {"video_title": video_title}).json()})
        if meta_data[video_title] != {}:
            video_title = meta_data[video_title][list(meta_data[video_title].keys())[0]]['video_title']
            save_data(data=meta_data, file_name="music_meta_tags_list")
        else:
            video_title = video_title.replace(".mp4", "")
        data[s] = {"video_title": video_title, "video_url": video_url}
    return meta_data, data


def get_data_list():
    get_data = lambda path: json.load(open(path))['data_list']
    data = {}
    for path in containers:
        data_list = get_data(path=f"{path}/data_list.json")
        for song in data_list:
            video_title = song['video_title'].replace('.mp4', '')
            data[video_title] = song['video_url']
    titles = list(data.keys())
    titles.sort()
    return [{"video_title": title,
             "video_url": data[title]}
            for title in titles]


def get_music_data_list():
    _data_list = get_data_list()
    music_meta_tags_list, music_data_list = get_meta_data(data=_data_list)
    music_template_list = dict(header=header_template, data=[table_template(index=s+1,
                                                                            video_title=music_data_list[s]['video_title'])
                                                             for s in range(len(music_data_list))])
    save_data(data=dict(music_data_list=music_data_list), file_name="music_data_list")
    save_data(data=music_template_list, file_name="music_template_list")
    return dict(music_data_list=music_data_list), music_template_list, music_meta_tags_list
