from sys import argv
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from time import ctime
path = Path(__file__).parent
args = argv[1:]


def getdate():
    dt = ctime()
    date = list(filter(lambda e: e != "", dt.split()))
    t = date[3].split(":")
    today = dict(
        day=int(date[2]), month=date[1], year=int(date[4]),
        hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2])        
    )
    for i in ("hours", "minutes", "seconds"):
        s = str(today[i])
        if len(s) == 1:
            today[i] = f"0{s}"
    return "{day}-{month}-{year}, {hours}:{minutes}:{seconds}".format(**today)    


class Env:
    file = path.joinpath(".env")   

    @classmethod
    def get(cls, key):
        cls.update()
        return environ.get(key)
        
    @classmethod
    def set(cls, key, value):
        data = dict()
        for line in cls.file.open().readlines():
            if line.endswith("\n"):
                line = line[:-1]
            x = line.split("=")
            data[x[0]] = x[1]
        data["last-update"] = getdate()
        data[key] = value
        cls.file.open("w").write("\n".join([
            f"{k}={v}" for k, v in data.items()
        ]))
        cls.update()
        
    @classmethod
    def update(cls):
        load_dotenv(cls.file)


if __name__ == "__main__":
    if len(args) == 2:
        if args[0] == "get":
            print(Env.get(args[1]))
    elif len(args) == 3:
        if args[0] == "set":
            Env.set(args[1], args[2])

