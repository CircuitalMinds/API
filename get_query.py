import requests
import yaml


def yaml_loader(path):
    return yaml.load(open(path), Loader=yaml.FullLoader)


def get_request(url, data=None):
    if data is None:
        response = requests.get(url).json()
        print(response)
        return response
    else:
        response = requests.get(url, data).json()
        print(response)
        return response


class API:

    settings = yaml_loader(path='./_config.yml')['api']
    url = f'http://{settings["host"]}:{settings["port"]}/get'

    def query_book(self, name, option):
        books = {
            "user_register": ["username", "password"],
            "music_app": ["video_url", "video_title", "video_image"],
            "blog": ["title", "date", "content", "picture"],
            "jupyter_app": ["title", "topic", "module", "location", "resources"]
        }
        query_url = f'{self.url}/{name}/{option}'
        if option == 'get':
            get_request(url=query_url)
        else:
            get_request(
                url=query_url,
                data={
                    key: 'test_' + key for key in books[name]
                }
            )

