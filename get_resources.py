def get_lib(name):
    if name == 'file_handlers':
        from utils import FileHandlers
        return FileHandlers
    if name == 'system_browser':
        from utils import SystemBrowser
        return SystemBrowser()
    if name == "video_manager":
        from python_resources import video_lib
        video_manager = video_lib.__dict__["video_manager"](path="../music_containers")
        video_manager.set_containers()
        return video_manager
    if name == 'finders':
        from python_resources import video_lib
        return video_lib.Finders()
