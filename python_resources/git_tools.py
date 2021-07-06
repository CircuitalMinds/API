import subprocess
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Git-Commands'


class Color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = Color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n''' + Color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def git_commands(command):

    def clone(user, repo):
        print("\nYou will be asked for the user first and then the repository name.\n")
        user = input("User: ")
        __user__ = f'{user}'
        repo = input("Repository: ")
        __repo__ = f'{repo}'
        print("\nChoose the local path for your clone.")
        local = input("Local path: ")
        local_path = f'{local}'
        subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])

    def commit():
        message = input("\nType in your commit message: ")
        commit_message = f'{message}'
        run("commit", "-am", commit_message)
        run("push", "-u", "origin", "master")

    def branch():
        branch = input("\nType in the name of the branch you want to make: ")
        br = f'{branch}'
        run("checkout", "-b", br)
        choices = lambda select_choice: dict(
            y=run("push", "-u", "origin", br), n=print("\nOkay, goodbye!\n")
        )[select_choice] if select_choice in ['y', 'n'] else print("\nInvalid command! Use y or n.\n")
        choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
        choice = choice.lower()
        choices(choice)

    def pull():
        print("\nPulls changes from the current folder if *.git is initialized.")
        choices = lambda select_choice: dict(
            y=run('pull'), n=print("\nOkay, goodbye!\n")
        ) if select_choice in ['y', 'n'] else print("\nInvalid command! Use y or n.\n")
        choice = input("\nDo you want to pull the changes from GitHub? (y/n): ")
        choice = choice.lower()
        choices(choice)

    fetch = lambda: [print("\nFetches changes from the current folder."), run('fetch')]
    merge = lambda: run("merge", input("\nType in the name of your branch: "))
    reset = lambda: run("reset", input("\nType in the name of your file: "))
    blame = lambda: run("blame", input("\nType in the name of the file: "))

    def stash():
        print("\nDo you want to save, list, pop, show, branch, clear or drop? ")
        cmd = 'save, li, pop, show, branch, clear and drop'
        print("\nCommands to use: " + cmd)
        choice = input("\nType in the command you want to use: ")
        choice = choice.lower()
        choices = lambda select_choice: dict(
            save=run("stash", "save", input("\nType in your stash message: ")),
            li=run("stash", "li"),
            pop=run("stash", "pop"),
            show=run("stash", "show", "-p"),
            branch = run("stash", "branch", input("\nType in the name of the branch you want to stash: ")),
            clear = run("stash", "clear"),
            drop = run("stash", "drop")
        )[select_choice] if select_choice in [
            'save', 'li', 'pop', 'show', 'branch', 'clear', 'drop'
        ] else print("\nNot a valid command!")
        choices(choice)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")
    choices = [
        'clone', 'commit', 'branch', 'pull', 'fetch', 'merge', 'reset', 'blame', 'stash'
    ]
    print("Commands to use: " + ', '.join(choices))
    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()
    git_commands(choose_command) if choose_command in choices else print(
        "\nNot a valid command!"
    ), print(
        "\nUse " + ', '.join(choices)
    )


push_repo = lambda path: subprocess.getoutput(' && '.join([
    f"cd {path}", "git init", "git add .", "git commit -m 'auto'", "git push"
]))
push_repo(path='../')