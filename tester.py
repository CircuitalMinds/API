import requests
import yaml

api = yaml.load(open("./_config.yml"), Loader=yaml.FullLoader)["api"]
select_data = dict(
    music_app={"repr": {"video_title": "video_title"}, "to_update": {"video_url": "video_url_update"},
               "data": {video: video for video in ["video_url", "video_title", "video_image"]}
               },
    jupyter_app={"repr": {"title": "title"}, "to_update": {"location": "location_update"},
                 "data": {nb: nb for nb in ["title", "topic", "module", "location", "resources"]}
                 },
    blog={"repr": {"title": "title"}, "to_update": {"picture": "picture_update"},
          "data": {post: post for post in ["title", "date", "content", "picture"]}
          },
    user_register={"repr": {"username": "username"}, "to_update": {"password": "password_update"},
                   "data": {user: user for user in ["username", "password"]}
                   }
)


def get(query, option, data=None):
    return requests.get(f"http://{api['host']}:{api['port']}/get/{query}/{option}", data).json()


def test_get():
    query_data = []
    for query in select_data.keys():
        # with_repr = select_data[query]["repr"]
        query_data.append(get(query=query, option="get"))
        # get(query=query, option="get", data=with_repr)
    return query_data


def test_add():
    for query in select_data.keys():
        data = select_data[query]["data"]
        get(query=query, option="add", data=data)


def test_delete():
    for query in select_data.keys():
        data = select_data[query]["repr"]
        get(query=query, option="delete", data=data)


def test_update():
    for query in select_data.keys():
        data = select_data[query]["repr"]
        data.update(select_data[query]["to_update"])
        get(query=query, option="update", data=data)


def tester_methods():
    initial_test = test_get()
    test_add()
    test_update()
    test_delete()
    final_test = test_get()
    if initial_test == final_test:
        return {"test": "successfully"}
    else:
        return {"test": "failed"}

print(test_get())