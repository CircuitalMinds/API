import requests


url = 'http://127.0.0.1:6000/get'
books = {
    "user_register": ["username", "password"],
    "music_app": ["video_url", "video_title", "video_image"],
    "blog": ["title", "date", "content", "picture"],
    "jupyter_app": ["title", "topic", "module", "location", "resources"]
}

def get_request():
    for book in books.keys():
        data = {key: 'test_' + key for key in books[book]}
        response_data = requests.get(f'{url}/{book}/add', data).json()
        print(response_data)

def get_query():
    for book in books.keys():
        response_data = requests.get(f'{url}/{book}/get').json()
        print(response_data)
