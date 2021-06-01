import os
import yaml


class GitApp:
    if os.path.isfile("../credentials.yml"):
        credentials = yaml.load(open("../credentials.yml"), Loader=yaml.FullLoader)['credentials']
        username, password = credentials['username'], credentials['password']
        os.environ["username"], os.environ["password"] = username, password
    else:
        username, password = None, None

    def __init__(self):
        self.username = GitApp.username
        self.password = GitApp.password

    def git_session(self):
        import os
        import subprocess
        sentence = "git init && git add . && git commit -m 'auto'"
        os.system(sentence)
        input(subprocess.getoutput("git push origin main").__str__() + f"{os.system(GitApp.username)}")

        return {"Response": "Success"}

    def gitpush_music(self):
        for j in range(1, 11):
            branch = "music_" + str(j)
            path = "../root_server/home/music/" + branch
            self.gitpush(path=path, branch=branch)
        self.gitpush()
        return {"Response": "success"}

    def gitpush(self, path=None, branch=None):
        import os
        sentence = "git init && git add . && git commit -m 'auto' && git push origin "
        if path is None and branch is None:
            os.system(sentence + "localhost")
        else:
            os.system("cd " + path + " $$ " + sentence + branch)