import requests
import json


class HeadTemplates:

    def __init__(self):
        self.url = "https://circuitalminds.github.io"
        self.url_git = "https://raw.githubusercontent.com/CircuitalMinds"
        self.robots = lambda href: f'<link rel="canonical" href="{href}" />'
        self.basic = lambda name, content: f'<meta name="{name}" content="{content}" />'
        self.open_graph = lambda prop, content: f'<meta property="{prop}" content="{content}" />'
        self.item_prop = lambda item, content: f'<meta itemprop="{item}" content="{content}" />'
        self.title = lambda title: f'<title> {title} </title>'
        self.script = lambda url: '<script>function onload() { ' + url + ' }</script>'
        self.html = lambda head, script: f'<!DOCTYPE html>\n<html lang="en">\n<head>\n{head}\n</head>\n<body onload="onload()"></body>\n{script}\n</html>'
                
        self.music_meta_tags = list(json.load(open("../musicApp/music_meta_tags_list.json")).values())
        self.playlist = json.load(open("../musicApp/music_data_list.json"))["music_data_list"]      
        self.songs = {self.playlist[s]["video_title"]: self.music_meta_tags[s] for s in range(len(self.playlist))}
        self.blog_posts = ["2020-09-08-hidokei.markdown", "2020-09-14-birthdays.markdown", "2020-10-08-fractalmind.markdown", "2020-12-28-circuital.markdown"]
        self.pyfullstack_posts = ["2020-10-16-data_analysis.md", "2020-10-16-engineering.md", "2020-10-16-introduction.md"]
        for song in list(self.songs.keys()):            
            template = self.build_music_template(song_data=self.songs[song], song=song)
            self.save_template(template=template, name=f'music/{song.replace("/", "")}')
        for post in self.blog_posts:            
            template, name = self.build_blog_template(post=post, section="blog")
            self.save_template(template=template, name=name)
        for post in self.pyfullstack_posts:
            template, name = self.build_blog_template(post=post, section="pyfullstack")
            self.save_template(template=template, name=name)
            
    def save_template(self, template, name):
        outfile = open(f'{name}.html', "w")
        outfile.write(template)
        outfile.close()

    def default(self):
        _template = {
            "basic": {
                "robots": "index, follow",
                "description": "Spinning out gracefully",
                "viewport": "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no",
                "author": "Alan Matzumiya"},
            "open_graph": {
                "og:title": "Circuital | Minds",
                "og:type": "website",
                "og:image": self.url_git + "/circuitalminds.github.io/main/img/Jungle3.png",
                "og:url": self.url,
                "og:site_name": "Circuital | Minds",
                "og:description": "Spinning out gracefully",
                "fb:app_id": "772020893629559"},
            "title": "CircuitalMinds | Home", "url": self.url}
        return _template

    def builder(self, data, url_redirect):
        template = ""
        template += self.robots(href=data['url']) + "\n"
        names, props = data["basic"].keys(), data["open_graph"].keys()
        for name in names:
            template += self.basic(name=name, content=data["basic"][name]) + "\n"
        for prop in props:
            template += self.open_graph(prop=prop, content=data["open_graph"][prop]) + "\n"
        if "itemprop" in list(data.keys()):
            itemprops = list(data["itemprop"].keys())
            for item in itemprops:
                template += self.item_prop(item=item, content=data["itemprop"][item]) + "\n"
        template += self.title(title=data["title"])
        script = self.script(url=url_redirect)
        return self.html(head=template, script=script)

    def build_music_template(self, song_data, song):
        data = self.default()
        data["itemprop"] = {}
        tags = song_data["meta_tags"]        
        data["title"] = f'MusicApp | {song}'        
        data["url"] = f"{self.url}/previews/music/{song}"
        for tag in list(tags.keys()):
            value = tags[tag]
            if "YouTube" in value:
                value = value.replace("YouTube", "CircuitalMinds")
            elif "@youtube" in value:
                value = value.replace("@youtube", "CircuitalMinds")
            key = tag.split("_")
            _tag = ""
            for t in key[1:]:
                _tag += t + ":"
            _tag = _tag[::-1][1:][::-1]
            if "name" in key[0]:
                data["basic"][_tag] = value
            elif "property" in key[0]:
                data["open_graph"][_tag] = value
            elif "itemprop" in key[0]:
                data["itemprop"][_tag] = value 
        data["open_graph"]["og:title"] = f'MusicApp | {song}'   
        url_redirect = f'window.location.href = "{self.url}/music?play_song={song}";'
        template = self.builder(data=data, url_redirect=url_redirect)
        return template

    def build_blog_template(self, post, section):
        url_request = f"{self.url_git}/{section}/main"
        data = self.default()
        _data = list(dict.fromkeys(requests.get(f"{url_request}/_posts/{post}").text.split("***")[0].split("\n")))
        _data.remove("---")
        _data.remove("")
        text = _data[-1].split('"')[1:]
        if '</h3>' in text[1]:
            text.remove(text[1])
        _post = {"description": text[0]}
        _data = _data[::-1][1:]
        for i in range(len(_data)):
            _dict = _data[i].split(": ")
            key = _dict[0]
            value = ""
            for v in _dict[1].split(" "):
                if v != "":
                    value += v + " "
            _post[key] = value[::-1][1:][::-1]
        name = f"{section}/{post.split('.')[0].split('-')[-1]}"
        url = f"{self.url}/previews/{name}"
        _title = _post["title"]
        title = {"blog": f'Blog | {_title}', "pyfullstack": f'PyFullStack | {_title}'}[section]
        data["title"] = title
        data["url"] = url
        data["basic"]["description"] = _post["description"]
        data["open_graph"]["og:image"] = f"{url_request}/img/{_post['image']}"
        data["open_graph"]["og:title"] = title
        data["open_graph"]["og:description"] = _post["description"]
        data["open_graph"]["og:url"] = url
        _url = f"{self.url}/{name}/"
        url_redirect = f'window.location.href = "{_url}";' 
        template, name = self.builder(data=data, url_redirect=url_redirect), f'./{name}' 
        return template, name


templates = HeadTemplates() 
