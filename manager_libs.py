import os


def get_lib(name):
    resources = __import__("python_resources")
    return resources.__dict__[name]


video_manager = get_lib(name="video_lib").video_manager(path="../music_containers")
video_manager.set_containers()
_containers = video_manager.containers_data["directories"]
container_names = list(video_manager.containers_data["directories"])


def get_size(path):
    files, total_size, factor = {}, 0.0, 1024 ** -2
    for name in os.listdir(path):
        file_path = f'{path}/{name}'
        file_size = float(os.stat(file_path).st_size * factor)
        total_size += file_size
        files[name] = {
            "path": file_path,
            "size": file_size
        }
    return dict(files=files, total_size=total_size)


def files_sample(size_max=100.0):
    from random import sample
    files = get_size("../music_containers/waiting_files")["files"]
    samples_data = list(files)
    select_sample = {}
    cumulative_size = 0.0
    for name in sample(samples_data, len(samples_data)):
        cumulative_size += files[name]["size"]
        if cumulative_size < size_max:
            select_sample[name] = files[name]
        else:
            break
    return select_sample


def is_container_key(strings, tester):
    from string import ascii_lowercase
    letters = [y for y in ascii_lowercase]
    new_strings = strings.lower()
    for substring in strings.lower():
        if substring not in letters:
            new_strings = new_strings.replace(substring, "")
    return new_strings[0] == tester.split("_")[-1][0]


def push_handler():
    from time import sleep
    check_restrictions = video_manager.check_restrictions
    containers = {
        x: {"path": video_manager.containers_data["directories"][x], "files": {}}
        for x in list(video_manager.containers_data["directories"])
    }
    do_push = lambda path: [
        print(' && '.join([f"cd {path}", command])) for command in [
            ' && '.join(["git init", "git add .", "git commit -m 'auto'"]), "git push"
        ]
    ]
    sample_data = files_sample()
    while len(sample_data) != 0:
        for name in sample_data:
            if sample_data[name]["size"] < video_manager.size_limits["size_max"]:
                for letter in list(containers):
                    if is_container_key(name, letter):
                        if check_restrictions(check_id=letter.split('_')[-1]) == "success":
                            print("restrictions: success")
                            containers[letter]["files"][name] = sample_data[name]
            else:
                print(sample_data[name]["path"], sample_data[name]["path"].replace("waiting_files", "rejected_files"))
        while any([containers[i]["files"] != {} for i in list(containers)]):
            for n in list(containers):
                removes_data = []
                container = containers[n]
                for file in container["files"]:
                    file_data = container['files'][file]
                    removes_data.append(file)
                    do_push(f"{file_data['path']}")
                for r in removes_data:
                    container['files'].pop(r)
                    removes_data.remove(r)
            sleep(2)
        sample_data = files_sample()
        print(sample_data)



push_handler()



