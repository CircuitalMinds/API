def get_lib(name):
    if name == "video_lib":
        from python_resources import video_lib
        video_manager = video_lib.__dict__["video_manager"]
        video_manager.finders = {
            "google_search": video_lib.google_search,
            "wikipedia": video_lib.wikipedia,
            "youtube": video_lib.youtube
        }
        return video_manager


