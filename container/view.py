from container import Videos, Pictures
from flask import redirect, url_for, abort, Blueprint, jsonify
container = Blueprint("container", __name__)
container_names = ("videos", "pictures")


def json_response(data):
    return jsonify(data)


@container.route("/container/")
@container.route("/container/<name>/")
def container_root(name=None):
    if name in container_names:
        return redirect(url_for(f"{name}_view"))
    else:
        abort(404)


@container.route("/container/videos/")
@container.route("/container/videos/<folder>/")
def videos_view(folder=None):
    videos = Videos()
    if folder:
        if folder in videos.ids:
            return jsonify(videos.git_content(folder))
        else:
            abort(404)
    else:
        return jsonify(folders=videos.ids)


@container.route("/container/pictures/")
@container.route("/container/pictures/<folder>/")
def pictures_view(folder=None):
    if folder:
        if folder in Pictures.ids:
            return jsonify(name=folder, content=[])
        else:
            abort(404)
    else:
        return jsonify(folders=Pictures.ids)


'''

def videos_update_all():
    gitdata = {}
    files = {}
    for i in cls.ids:
        gitdata[i] = cls.git_content(i)
        files[i] = cls.get_folder(i)
    save_json(
        folder_data.joinpath("videos-git-content.json"),
        gitdata,
        ensure_ascii=True
    )
    save_json(
        folder_data.joinpath("videos-files.json"),
        files,
        ensure_ascii=True
    )
    return jsonify(dict(files=files, **{"git-content": gitdata}))

'''
