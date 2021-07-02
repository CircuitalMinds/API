



"""

tree = directory_tree(path='./', by_filter='directory')
for i in tree:
    print(i)
def filetype(object_data, restriction):
    import os
    is_file = lambda key: any(key.lower().endswith(object_data[key].split('.')[-1]) for restriction in list(object_data))
    for key in list(object_data):
        if is_file:
            return True
        else: return False

    print(filetype_restriction(data, 'json'))
data = {}


def get_data(content_data):
    out_data = {"files": {}, "directories": {}}
    for ci in content_data:
        out_data["files"].update({ci["name"]: ""}) if ci["type"] == "file" else out_data["directories"].update(
            {ci["name"]: {s["name"]: "" if s["type"] == "file" else {si["name"]: "" for si in s["contents"]} for s in ci["contents"]}}
        )
    return out_data

def set_content(name):
    content_data = get_data(contents[name])
    data.update({
        name: get_data(contents[name])
    }) if any([v != {} for v in content_data.values()]) else data.update({
        name: ''
    })


for name in contents.keys():
    set_content(name)

data = {"a": 1, "b": 2, "c": 10}
"""