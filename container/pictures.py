from module.utils import getjson, save_json
from pathlib import Path
giturl = "https://github.com"
gituser = "alanmatzumiya"


class Pictures:
    folder_data = Path(__file__).parent.joinpath("data/pictures")
    ids = sorted(
        i for i in Path.home().joinpath(
            "Pictures/containers"
        ) if i.is_dir()
    )

    def __init__(self, ident):
        self.id = ident
        self.name = f"pictures_{ident}"
        self.url = f"{giturl}/{gituser}/{self.name }"
        self.content = []
        self.totalsize = 0.0

    def getdata(self):
        jsonfile = self.folder_data.joinpath(f"{self.id}.json")
        if jsonfile.exists():
            self.content = getjson(jsonfile)




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






def url_content(ident):
    return f"{env['GIT-URL']}/circuitalmynds/music_{ident}/blob/main/videos"
class Pictures:
    path = home_path.joinpath("Pictures/containers")
    ids = sorted([i.name for i in path.iterdir() if i.is_dir()])
    route = "/containers/pictures/"
