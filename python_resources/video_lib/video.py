class Video:
    google_search = None
    wikipedia_search = None

    def __init__(self, title):
        self.title = title
        self.lyrics = dict()
        self.info = dict()
        self.get_lyrics = lambda: self.lyrics.update(Video.google_search(title=title))
        self.get_info = lambda: self.info.update(Video.wikipedia_search(title=title))
