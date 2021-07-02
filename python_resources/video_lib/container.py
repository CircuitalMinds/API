class Container:
    video = None

    def __init__(self, id, location):
        self.id = id
        self.location = location

    @property
    def video_list(self):
        videos = __import__('json').load(open(f'{self.location}/video_list.json'))
        return lambda get='titles': [title for title in videos.keys()] if get == 'titles' else videos

    @property
    def available_space(self):
        return __import__('json').load(
            open(f'{self.location}/info_container.json')
        )['available_space']

    @property
    def limit_sizes(self):
        file_data = __import__('json').load(open(f'{self.location}/info_container.json'))
        return {size: file_data[size] for size in ['size_max', 'total_size']}
