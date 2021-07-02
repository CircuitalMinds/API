import os
import subprocess
from python_resources import utils


class GitRepos:

    def __init__(self):
        self.path = '../'
        self.repositories = {}
        self.allowed_files = {
            "documents": ["pdf", "txt", "md", "html", "json", "yml"],
            "media": ["psd", "woff", "svg", "ttf", "ico", "png", "jpeg", "jpg", "gif", "mp4", "mp3"],
            "scripts": ["py", "js", "css", "ipynb", "php", "map", "less", "sqlite3"]
        }
        self.ignored_files = ["environment", ".git", "__pycache__", ".idea"]
        self.current_directory = {"files": {}, "directories": {}}
        self.file_handlers = dict(waiting_files={}, trash_files={}, rejected_files={})
        self.get_repositories(), self.set_file_handlers()

    def set_file_handlers(self):
        updater = lambda data: lambda: data.update(files=os.listdir(data["path"]))
        get_data = lambda data, path: data.update(dict(path=path, files=[], update=updater(data)))
        for name in list(self.file_handlers):
            get_data(
                data=self.file_handlers[name],
                path=self.join_path("../music_containers", path_right=name)
            )
            self.file_handlers[name]["update"]()

    def get_repositories(self):
        repos_data = utils.open_file(self.path + 'repositories.yml')
        for key in list(repos_data):
            if key == 'music_containers':
                self.repositories[key] = {
                    section: {
                        container: f"{self.path + key}/{section}/{container}"
                        for container in os.listdir(f"{self.path + key}/{section}")
                    } for section in list(repos_data[key])
                }
            else:
                self.repositories.update({key: {"path": self.path + key}})
        return self.repositories

    def goto(self, path):
        self.current_directory = {"files": {}, "directories": {}}
        commands = " && ".join([
            f"cd {path}", "ls"
        ])
        add_data = lambda dir_path: self.current_directory["files"].update({
            dir_path.split("/")[-1]: dir_path
        }) if os.path.isfile(dir_path) else self.current_directory["directories"].update({
            dir_path.split("/")[-1]: dir_path
        })
        for name in subprocess.getoutput(commands).splitlines():
            add_data(dir_path=os.path.join(path, name))

    def from_current_directory(self, get_data):
        data_names = list(get_data)
        if data_names:
            send_data = []
            for name_i in data_names:
                if name_i in list(self.current_directory):
                    dataset = self.current_directory[name_i]
                    if get_data[name_i] == "all":
                        send_data.append(dataset)
                    elif get_data[name_i] in list(dataset):
                        send_data.append(dataset[get_data[name_i]])
                    else:
                        send_data.append(dataset)
            if len(send_data) == 1:
                return send_data[0]
            else:
                return [data_i for data_i in send_data]
        else:
            return self.current_directory

    def move_file(self, from_path, to_path):
        is_files = all([self.is_file(from_path), self.is_file(to_path)])
        if is_files:
            print(from_path, to_path)
        else:
            pass

    def commit(self, repo):
        if repo in self.repositories.keys():
            command = ' && '.join([
                f"cd {self.repositories[repo]['path']}", "git commit -m 'auto'"
            ])
            print(command)
        else:
            pass

    def push(self, repo):
        if repo in self.repositories.keys():
            command = ' && '.join([
                f"cd {self.repositories[repo]}", "git push"]
            )
            print(command)

    def push_engine(self, from_path, repos):
        if os.path.isdir(from_path):
            data = {"containers": {}}
            for name in list(repos):
                data["containers"][name] = {"files": {}, "path": repos[name]}
            for filename in os.listdir(from_path):
                for s in list(repos):
                    if self.is_container_key(filename, s):
                        data["containers"][s]["files"][filename] = git.join_path(
                            f'{data["containers"][s]["path"]}/videos', filename
                        )
            remove_files = lambda repo, sample: [
                data["containers"][repo]['files'].pop(fi) for fi in sample
            ]
            get_info = lambda sample: self.info_sample_files(sample)
            get_container_size = lambda path: sum([
                float(os.stat(f'{path}/{name}').st_size * 1024 ** -2) for name in os.listdir(path)
            ])
            push_repo = lambda path: [
               os.system(' && '.join([f"cd {path}", command])) for command in [
                    ' && '.join(["git init", "git add .", "git commit -m 'auto'"]), "git push"
                ]
            ]
            is_file = os.path.isfile
            def workflow(repo):
                repo_data = data["containers"][repo]
                repo_size = lambda: get_container_size(f'{repo_data["path"]}/videos')
                rm = os.rename
                size = repo_size()
                print(size)
                if size > 980.0:
                    remove_files(repo, repo_data["files"])
                else:
                    fpath = lambda fname: f'../music_containers/waiting_files/{fname}'
                    sample = {name: fpath(name) for name in list(repo_data["files"])[:5]}
                    info = get_info(sample)
                    rejected, no_rejected = info["rejected"], info["no_rejected"]
                    for name in rejected:
                        in_path, out_path = [
                            fpath(fname=name), fpath(fname=name).replace("waiting_files", "rejected_files")
                        ]
                        if is_file(in_path) and is_file(out_path) is False:
                            rm(in_path, out_path)
                        else:
                            rm(in_path, in_path.replace("waiting_files", "trash_files"))
                    for name in no_rejected:
                        in_path, out_path = [fpath(fname=name), repo_data["files"][name]]
                        if is_file(in_path) and is_file(out_path) is False:
                            rm(in_path, out_path)
                        else:
                            rm(in_path, in_path.replace("waiting_files", "trash_files"))
                        if repo_size() > 980.0:
                            break
                    remove_files(repo, sample)

            def no_empty_repos():
                repo_names = []
                for r in list(data["containers"]):
                    if len(list(data["containers"][r]["files"])) != 0:
                        repo_names.append(r)
                return repo_names
            def init_push(timer):
                from time import sleep
                repo_names = no_empty_repos()
                while len(repo_names) != 0:
                    for repo in repo_names:
                        workflow(repo)
                        push_repo(data["containers"][repo]["path"])
                    repo_names = no_empty_repos()
                    sleep(timer)
            data["init_push"] = init_push
            return data
        else:
            return None


    def get_container_files(self, section, container, data_name):
        container_path = self.repositories["music_containers"][section][container]
        self.goto(path=container_path)
        data_path = self.from_current_directory(get_data={"directories": data_name})
        self.goto(path=data_path)
        return self.from_current_directory(get_data={"files": "all"})

    def get_container_section(self, section):
        section_name = f"section_{section}" if type(section) == int else section
        if section_name in list(self.repositories["music_containers"]):
            containers = self.repositories["music_containers"][section_name]
            data = {}
            for name in list(containers):
                data[name] = {"files": {}, "path": containers[name]}
            return data
        else:
            return {}

    @staticmethod
    def info_file(file_path):
        size = float(os.stat(file_path).st_size * 1024 ** -2)
        is_rejected = size > 50.0
        return dict(size=size, is_rejected=is_rejected)

    @staticmethod
    def info_sample_files(files):
        rejected = []
        no_rejected = []
        for name in list(files):
            size = float(os.stat(files[name]).st_size * 1024 ** -2)
            if size > 49.5:
                rejected.append(name)
            else:
                no_rejected.append(name)
        return {"rejected": rejected, "no_rejected": no_rejected}

    @staticmethod
    def join_path(path_left, path_right):
        return os.path.join(path_left, path_right)

    @staticmethod
    def is_container_key(strings, tester):
        from string import ascii_lowercase
        letters = [y for y in ascii_lowercase]
        new_strings = strings.lower()
        for substring in strings.lower():
            if substring not in letters:
                new_strings = new_strings.replace(substring, "")
        return new_strings[0] == tester.split("_")[-1][0]

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)



git = GitRepos()
repos = git.repositories["music_containers"]["section_1"]
data = git.push_engine(from_path="../music_containers/waiting_files", repos=repos)
data["init_push"](timer=1)