from .video_manager import VideoManager
from .container import Container
from . import youtube, finders


class Finders:
    pass


Finders.wikipedia = finders.wikipedia_search
Finders.google_search = finders.google_search
Finders.youtube = youtube
video_manager = VideoManager
