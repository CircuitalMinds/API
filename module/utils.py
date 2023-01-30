from .shell import CLI
from time import ctime
from os.path import getctime
from pathlib import Path
from json import load, dumps
from yaml import full_load
from csv import DictReader
jsonconfig = dict(
    indent=4,
    sort_keys=True,
    ensure_ascii=False
)

hostname = CLI.input("hostname -I", getout=True)[0]
url_root = f"http://{hostname}"


def dumper(datastr: str, **config):
    settings = jsonconfig.copy()
    settings.update(config)
    return dumps(datastr, **settings)


def getjson(filepath):
    return load(Path(str(filepath)).open())


def get_yaml(filepath):
    return full_load(Path(str(filepath)).open())


def save_json(filepath, data, **config):
    Path(str(filepath)).open("w").write(dumper(data, **config))


def opencsv(filepath):
    return [
        row for row in DictReader(
            Path(str(filepath)).open()
        )
    ]


def getdate(path=None, formatted=False):
    dt = ctime(getctime(Path(str(path)))) if path else ctime()
    if formatted:
        return dt
    else:
        date = list(filter(lambda e: e != "", dt.split()))
        t = date[3].split(":")
        return dict(
            day=int(date[2]), month=date[1], year=int(date[4]),
            hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2])
        )


def get_files(path):
    path = Path(str(path))
    content = []
    files = [i for i in path.iterdir() if i.is_file()]
    for file in files:
        content.append(dict(
            filename=file.name,
            size=file.stat().st_size * 1.0e-6,
            path=str(file)
        ))
    return content
