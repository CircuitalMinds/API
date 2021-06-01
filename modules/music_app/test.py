import json
import os

path = "../../music_containers"
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

def get_songs():
    meta = {}
    data = []
    for cont in data_containers:
        data.extend(os.listdir(f"{path}/{cont}/videos"))
    for n in range(1, 8):
        meta.update(json.load(open(f"{path}/pendientes/music_{n}/music_data.json")))
    for s in meta:
        test = [s in t for t in data]
        new_data
        if any(test):
            r = data[test.index(True)]
            print(r, meta[s])

get_songs()