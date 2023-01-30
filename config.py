from os import environ
from pathlib import Path
from dotenv import load_dotenv
from module.utils import getjson
conf, app_home = dict(), Path(__file__).parent
load_dotenv(app_home.joinpath(".env"))
if environ.get("APP-ENV") == "production":
    conf = getjson(app_home.joinpath("conf/production.json"))
else:
    conf = getjson(app_home.joinpath("conf/development.json"))


class Route:
    mapping = dict(
        container=dict(
            pictures="/container/pictures/",
            videos="/container/videos/"
        ),
        drive=dict(
            storage=dict(
                documents="/drive/storage/documents/",
                pictures="/drive/storage/pictures/",
                videos="/drive/storage/videos/"
            ),
            trash="/drive/trash/"
        ),
        jupyter=dict(
            notebooks=dict(
                intro="/jupyter/notebooks/intro/",
                engineering="/jupyter/notebooks/engineering/",
                data_science="/jupyter/notebooks/data-science/"
            ),
            dataset="/jupyter/dataset/"
        ),
        user=dict(
            auth="/user/auth/",
            login="/user/login/",
            register="/user/register/"
        ),
        youtube=dict(
            search="/youtube/search/",
            watch="/youtube/watch/",
            download="/youtube/download/"
        )
    )
