import os
import json



path = "../../music_containers/"
def get_music():
    get_data = lambda n: json.load(open(f"{path}/pendientes/music_{n}/music_data.json"))
    get_songs = lambda n: os.listdir(f"{path}/music_container_1{n}/videos")
    for n in range(1, 8):
        data = get_data(n)
        new_data = json.load(open(f"{path}/music_container_1{n}/meta_tags.json"))
        songs = get_songs(n)
        for s in data:
            test = [s in t for t in songs]
            if any(test):
                new_data.update({s: data[s]})
        with open(f"{path}/music_container_1{n}/meta_tags.json", "w") as outfile:
            json_file = json.dumps(new_data, indent=4, sort_keys=True)
            outfile.write(json_file)
            outfile.close()
get_music()