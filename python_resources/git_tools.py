import subprocess
import requests
from bs4 import BeautifulSoup as Analyzer
from utils import Printer, FileHandlers
style = Printer.text_style

git = 'https://github.com'
organization = 'CircuitalMinds'
proprietary = 'alanmatzumiya'
style(organization, color='cyan', font='slant')
style("Organization:", color='magenta'), style(organization)
style("Proprietary:", color='magenta'), style(proprietary)
info_data = FileHandlers.open_file(path='info.json')
options = [
        'clone', 'commit', 'branch', 'pull', 'fetch', 'merge', 'reset', 'blame', 'stash'
]
style(f'\nrepositories:', color='magenta')
[style(f"  {repo}: {url}") for repo, url in info_data['repositories'].items()]
style(f'\ncommand options:', color='magenta')
[style(f'  {i}. {opt}') for i, opt in enumerate(options)]


def run(*args):
    print(list(args))
    """
    return subprocess.check_call(['git'] + list(args))
    """


def get_repositories():
    request_data = Analyzer(requests.get(f'{git}/{organization}').text, 'html.parser')
    repos = request_data.find_all('a', {'itemprop': 'name codeRepository'})
    data = dict(repositories={
        link.text.split()[0]: git + link.get("href") for link in repos
    })
    info_data.update(data)
    FileHandlers.save_file(path='info.json', data=info_data)
    return info_data


commit = lambda message: f'git commit -m "{message}"'
pull = lambda: "pull"
fetch = lambda: [print("\nFetches changes from the current folder."), run('fetch')]
merge = lambda: run("merge", input("\nType in the name of your branch: "))
reset = lambda: run("reset", input("\nType in the name of your file: "))
blame = lambda: run("blame", input("\nType in the name of the file: "))


def create_repo(name):
    return ' && '.join([
        f'echo "# {name}" >> README.md', "git init",
        "git add README.md",
        commit('first commit'),
        "git branch -M main",
        f"git remote add origin {git}/{organization}/{name}.git"
        "git push -u origin main"
    ])


def push_repo(name):
    return ' && '.join([
        f'git remote add origin {git}/{organization}/{name}.git',
        'git branch -M main',
        'git push -u origin main'
    ])


def stash():
    choices = {
        'save': lambda: "\nType in your stash message: ",
        'li': '', 'pop': '',
        'show': '-p',
        'branch': lambda: "\nType in the name of the branch you want to stash: ",
        'clear': '', 'drop': ''
    }
    style(f'\nselect choice:', color='magenta')
    [style(f'  {i}. {opt}') for i, opt in enumerate(choices)]

    on_select = lambda selected: ["stash", selected] + [
        input(choices[selected]()) if callable(choices[selected]) else choices[selected]
    ]
    choice = input("\nType in the command you want to use: ")
    commands = on_select(choice.lower())
    if '' in commands:
        commands.remove('')
    run(commands)
