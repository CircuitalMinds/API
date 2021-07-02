import os


def setup_repos_data():
    repos = {}
    dirs = os.listdir(f"../")
    dirs.remove("repositories.yml")
    dirs.remove("server_config.yml")
    repos.update({name: {"path": f"../{name}"} for name in dirs})
    for name in dirs:
        for sub_dir in os.listdir(repos[name]["path"]):
            sub_path = f'{repos[name]["path"]}/{sub_dir}'
            sub_data = {sub_dir: None}
            if os.path.isfile(sub_path):
                sub_data.update({sub_dir: sub_path})
            else:
                sub_data.update({
                    sub_dir: {
                        n: f'{sub_path}/{n}' if os.path.isfile(f'{sub_path}/{n}')
                        else {
                            s: f'{sub_path}/{n}/{s}' for s in os.listdir(f"{sub_path}/{n}")
                        } for n in os.listdir(sub_path)
                    }
                })
            repos[name].update(sub_data)
    return repos


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
    sample_data = files_sample()
    data = {
        c: {} for c in list(setup_repos_data()["music_containers"]["section_0"])
    }
    do_push = lambda path: [
        print(' && '.join([f"cd {path}", command])) for command in [
            ' && '.join(["git init", "git add .", "git commit -m 'auto'"]), "git push"
        ]
    ]
    for name in sample_data:
        for letter in list(data):
            if is_container_key(name, letter):
                data[letter][name] = sample_data[name]
    while any([data[i] != {} for i in list(data)]):
        for n in list(data):
            removes_data = []
            for file in data[n]:
                removes_data.append(file)
                do_push(data[n][file]["path"])
            for r in removes_data:
                data[n].pop(r)
                removes_data.remove(r)
        sleep(2)
    print(data)

push_handler()
