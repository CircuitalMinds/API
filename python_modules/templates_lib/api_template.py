import os
import json
from .api_music import MusicApp
from .api_console import ConsoleApp
from .api_math import MathApp
from .api_youtube import YouTubeApp
from .api_jupyter import JupyterApp
from .api_github import GitApp


def save_template(data, to_path, name):
    from_path = './api_modules'
    with open(f"{from_path}/{to_path}/{name}.json", "w") as outfile:
        json_file = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(json_file)
        outfile.close()


class Apps:

    def __init__(self, template_folder, storage_folder):
        self.music_app = MusicApp(path=template_folder)
        self.console_app = ConsoleApp(path=template_folder)
        self.storage_app = json.load(open('./api_modules/desktop_app/storage_template.json'))
        self.math_app = MathApp
        self.git_app = GitApp
        self.youtube_app = YouTubeApp
        self.jupyter_app = JupyterApp


class DesktopTemplate:

    def __init__(self, static):
        self.static = static
        self.template = 'desktop.html'
        self.notifies = []
        self.notifies.extend(self.get_posts())
        save_template(data=dict(notifies=self.notifies), to_path='desktop_app', name='notifies')

    @staticmethod
    def notify_structure():
        notify = dict(
            icon='', title='', primary_content='', date='', social_network='Facebook'
        )
        return notify

    def get_posts(self):
        to_path = '../circuitalminds.github.io/_posts'
        to_save = []
        posts = os.listdir(to_path)
        for post in posts:
            get_data = open(f'{to_path}/{post}').read()
            post_data = get_data.split('---')[1]
            to_keys = ['title', 'date', 'image', 'tags']
            to_data = {}
            notify = self.notify_structure()
            for key in to_keys:
                value = post_data.split(f'\n{key}:  ')[1].split('\n')[0]
                if value.startswith(' '):
                    value = value[1:]
                to_data[key] = value
            notify['title'] = to_data['title']
            notify['date'] = to_data['date']
            notify['icon'] = f'{self.static["images"]}/blog/{to_data["image"]}'
            notify['primary_content'] = to_data['tags']
            to_save.append(self.get_notify(data=notify))
        return to_save

    @staticmethod
    def get_notify(data):
        img = f'\n<img class="icon" src="{data["icon"]}">\n'
        title = f'<div class="title"> {data["title"]} </div>\n'
        primary_content = f'<div class="content"> {data["primary_content"]} </div>\n'
        secondary_content = f'<div class="secondary"> {data["date"]} &bull; {data["social_network"]} </div>\n'
        charm_notify = f'<div class="charm-notify"> {img} {title} {primary_content} {secondary_content} </div>'
        return charm_notify


class TemplateEngine:

    def __init__(self, assets):
        self.apps = Apps(template_folder=assets['template_folder'], storage_folder=assets['storage_folder'])
        self.desktop = DesktopTemplate(static=assets['static'])
        self.data = dict(title="CircuitalMinds", static=assets['static'],
                         directories=self.apps.storage_app['home'], notifies=self.desktop.notifies)
        self.assets = assets

    def get_apps(self):
        apps = []
        template_folder = self.assets['template_folder']
        for app in os.listdir(template_folder):
            if app.endswith("app.html"):
                name = app.replace('.html', '')
                c = name.split('_')[0]
                caption = c[0].upper() + c[1:]
                init_script = f"Apps['{name}'].open_script()"
                app_data = dict(name=name, caption=caption, init_script=init_script)
                apps.append(app_data)
        return apps

    def get_assets(self):
        metro = self.assets['metro']
        assets = dict()
        ajax = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
        assets["metro"] = dict(css=dict(href=f'{metro["css"]}/metro-all.css', rel='stylesheet'),
                               js=dict(src=f'{metro["js"]}/metro.js'))
        assets['ajax'] = {'src': ajax}
        return assets

    @staticmethod
    def get_meta_tags():
        git_url = "https://circuitalminds.github.io"
        git_content = "https://raw.githubusercontent.com/CircuitalMinds/circuitalminds.github.io/main"
        name_list = {'robots': 'index, follow',
                     'description': 'Spinning out gracefully',
                     'viewport': 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no',
                     'author': 'Alan Matzumiya'}
        prop_list = {'og:title': 'Circuital | Minds',
                     'og:type': 'website',
                     'og:image': f'{git_content}/img/Jungle3.png',
                     'og:url': git_url,
                     'og:site_name': 'Circuital | Minds',
                     'og:description': 'Spinning out gracefully',
                     'fb:app_id': '772020893629559'}
        meta_tags = []
        for n in name_list.keys():
            meta_tags.append({'name': n, 'content': name_list[n]})
        for p in prop_list.keys():
            meta_tags.append({'property': p, 'content': prop_list[p]})
        return meta_tags

    @staticmethod
    def set_buttons(button_list=None, script_list=None):
        if button_list is None:
            button_list = ['rocket', 'user', 'cog']
        if script_list is None:
            script_list = [f'console.log("{j}")' for j in range(len(button_list))]
        get_html = lambda icon_name: f'<span id="{icon_name}" class="mif-{icon_name}"></span>'
        buttons = []
        for n in range(len(button_list)):
            buttons.append(dict(html=get_html(icon_name=button_list[n]),
                                onclick=script_list[n]))
        return buttons

    def settings_data(self):
        icon = 'windows'
        templates = {}
        template_folder = self.assets['template_folder']
        for app in os.listdir(template_folder):
            if app.endswith('app.html'):
                templates[app.replace('.html', '')] = open(f'{template_folder}/{app}').read()
        json_objects = {}
        set_apps = dict(
                music_app=dict(
                    title='Music App',
                    icon=icon,
                    buttons=self.set_buttons(
                        button_list=['volume-minus', 'volume-plus',
                                     'previous', 'play', 'next'],
                        script_list=['setVolume("minus")',
                                     'setVolume("plus")',
                                     'setVideo("back")',
                                     'setPlayer(Play.className.replace("mif-", ""))',
                                     'setVideo("next")']),
                    template=templates['music_app'],
                    current_song=0,
                    song_data=self.apps.music_app.get_random_list()
                ),
                console_app=dict(
                    title="Python Console",
                    icon=icon,
                    template=templates['console_app'],
                    buttons=self.set_buttons()
                ),
                storage_app=dict(
                    title='Storage',
                    icon=icon,
                    template=self.apps.storage_app,
                    buttons=self.set_buttons()
                )
        )
        for name in set_apps.keys():
            json_objects[name] = set_apps[name]
        return json.dumps(json_objects)

    def build_template(self):
        meta_tags = []
        apps = []
        for meta in self.get_meta_tags():
            meta_tags.append(meta)
        for app in self.get_apps():
            apps.append(app)
        self.data.update({'meta_tags': meta_tags})
        self.data.update({'apps': apps})
        self.data.update(self.get_assets())


