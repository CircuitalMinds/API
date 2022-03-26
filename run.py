from os import system
from os.path import isdir
from sys import argv
from json import load, dumps
args = argv[1:]


def settings_update(mode):
    data = load(open("settings.json"))
    if mode == "production":
        data["server"] = {
            "host": "https://circuitalminds.heroku.com",
            "port": 80,
            "debug": False
        }
    elif mode == "development":
        data["server"] = {
            "host": "192.168.50.7",
            "port": 8888,
            "debug": True
        }
    with open("settings.json", "w") as f:
        f.write(dumps(
            data, **dict(
                indent=4,
                sort_keys=True,
                ensure_ascii=False
            )
        ))


if __name__ == "__main__":
    if "app" in args:
        from app import run
        run()
    if "install" in args:
        if not isdir("environment"):
            system("bash install.sh environment")
        system("bash install.sh requirements")
    if "update" in args:
        settings_update("production")
        system("bash update.sh")
        settings_update("development")
