import json


class DesktopApp:

    def __init__(self):
        self.apps = {"music_app": "",
                     "jupyter_app": "",
                     "storage_app": "",
                     "console_app": ""}
        self.apis = {"api_math": "",
                     "api_youtube": "",
                     "api_github": ""}
        self.static = {}

    @property
    def template(self):
        return 'desktop.html'

    def notify_template(self):
        return json.load(
            open("./desktop_app/object_templates/notify.json"))


    @staticmethod
    def import_module(**module_data):
        module = __import__(module_data['name']).__dict__[module_data['class']]
        return module


desk_app = DesktopApp()
print(desk_app.template)
