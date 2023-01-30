from os import system, environ
from pathlib import Path
from dotenv import load_dotenv
from subprocess import getoutput
cpath = Path(__file__).parent
load_dotenv(cpath.parent.joinpath(".env"))
src_folder = cpath.joinpath("bash")
environ["TERM"] = "xterm"


class CLI:
    env = {}

    def __init__(self):
        self.scripts = list(src_folder.iterdir())
        self.refresh()

    def runscript(self, path, arg, *args):
        path = src_folder.joinpath(str(path))
        self.input(f"bash {str(path)} {arg} {' '.join(args)}")

    def refresh(self):
        self.env = {
            "app-env": dict(environ),
            "shell-env": {}
        }
        for e in self.input("env", getout=True):
            k, v = e.split("=")[:2]
            self.env["shell-env"][k] = v

    @classmethod
    def input(cls, command, **opts):
        if opts.get("getout"):
            return cls.output(command)
        else:
            system(command)

    @staticmethod
    def output(command):
        lines = getoutput(command).strip().splitlines()
        return [
            line for line in lines if line != ""
        ]

    @staticmethod
    def clear():
        system("clear")

    @staticmethod
    def do_sleep(t, unit="s"):
        system(
            f"sleep {str(t)}{unit if unit in ('s', 'm', 'h', 'd') else 's'}"
        )


if __name__ != "__main__":
    CLI = CLI()
