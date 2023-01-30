from module.utils import getjson, save_json, CLI
from bs4 import BeautifulSoup
from requests import get
from os.path import join
from pathlib import Path
env = CLI.env["app-env"]
folder_data = Path(__file__).parent.joinpath("data")
home_path = Path(CLI.env["shell-env"]["HOME"])


class Videos:
    path = home_path.joinpath("Videos/containers")
    ids = sorted([i.name for i in path.iterdir() if i.is_dir()])
    route = "/containers/videos/"

    @staticmethod
    def url_content(ident):
        return f"{env['GIT-URL']}/circuitalmynds/music_{ident}/blob/main/videos"

    def get_folder(self, ident):
        info = dict(
            available_space=True,
            total_size=0.0,
            content=[],
            ready_to_push=True
        )
        if ident in self.ids:
            path = Videos.path.joinpath(ident)
            jsonpath = path.joinpath("info.json")
            files = list(path.joinpath("videos").iterdir())
            for file in files:
                datafile = dict(
                    name=file.name,
                    id=file.name.split(".mp4")[0][-11:],
                    size=file.stat().st_size * 1.0e-6,
                    path=str(file.relative_to(home_path.joinpath(
                        "Videos/containers"
                    ))),
                    url=f"{Videos.url_content(ident)}/{file.name}?raw=true"
                )
                info["content"].append(datafile)
                info["total_size"] += datafile["size"]
            if info["total_size"] > 9.5e2:
                info["available_space"] = False
                if info["total_size"] > 1.05e3:
                    info["ready_to_push"] = False
                for x in info["content"]:
                    if x.get("size") > 95.0:
                        info["ready_to_push"] = False
            save_json(jsonpath, info, ensure_ascii=True)
            return getjson(jsonpath)
        else:
            return info

    def git_content(self, ident):
        content = []

        if ident in self.ids:
            jsonfile = folder_data.joinpath(f"videos/{ident}.json")
            if not jsonfile.exists():
                page_url = join(env["GIT-URL"], f"circuitalmynds/music_{ident}/tree/main/videos")
                page_data = get(page_url).text
                links = list(filter(
                    lambda a: a.get("href").endswith(".mp4"),
                    BeautifulSoup(page_data, "html.parser").find("body").findAll("a")
                ))
                for i in links:
                    content.append(dict(
                        name=i.get("title"),
                        url=f'{env["GIT-URL"]}{i.get("href")}?raw=true'
                    ))
                save_json(jsonfile, content, ensure_ascii=True)
            content = getjson(jsonfile)
        return content

    @staticmethod
    def handler_files():
        jsonpath = folder_data.joinpath("videos-handler-files.json")
        path = home_path.joinpath("Videos/handler")
        waiting, rejected = [], []
        for file in list(path.joinpath("waiting").iterdir()):
            waiting.append(dict(
                name=file.name,
                id=file.name.split(".mp4")[0][-11:],
                size=file.stat().st_size * 1.0e-6,
                path=str(file)
                )
            )
        for file in list(path.joinpath("rejected").iterdir()):
            rejected.append(dict(
                name=file.name,
                id=file.name.split(".mp4")[0][-11:],
                size=file.stat().st_size * 1.0e-6,
                path=str(file)
                )
            )
        files = dict(waiting=waiting, rejected=rejected)
        save_json(
            jsonpath, files, ensure_ascii=True
        )
        return files


class Pictures:
    path = home_path.joinpath("Pictures/containers")
    ids = sorted([i.name for i in path.iterdir() if i.is_dir()])
    route = "/containers/pictures/"
