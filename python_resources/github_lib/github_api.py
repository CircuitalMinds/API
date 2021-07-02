import os
from string import ascii_lowercase

class Git:

    @staticmethod
    def get_repositories(path):
        repos = dict()
        containers = [
            {f'music_{ly}': path + f'music_containers/music_{ly}' for ly in ascii_lowercase},
            {f'music_{ly}1': path + f'music_containers/next_containers/music_{ly}1' for ly in ascii_lowercase}
        ]
        for container in containers:
            repos.update(container)
        repo_names = os.listdir(path)
        repo_names.remove('music_containers')
        repos.update({name:  path + name for name in repo_names})
        return repos

    @staticmethod
    def get_app(repositories_path):
        git = __class__()
        repositories = Git.get_repositories(path=repositories_path)
        git.__setattr__('repositories', repositories)
        git_function = lambda command: lambda name: os.system(
            f'cd {repositories[name]} && {command}') if name in repositories.keys() else f'repo with {name} not exists'
        commands = {k: git_function(v) for k, v in {
                'commit': "git init && git add . && git commit -m 'auto'",
                'push': 'git push',
                'pull': 'git pull'
            }.items()
        }
        for name in commands.keys():
            git.__setattr__(name, commands[name])
        return git
