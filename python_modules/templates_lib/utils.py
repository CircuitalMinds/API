'''
echo "# storage_app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/CircuitalMinds/storage_app.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/CircuitalMinds/storage_app.git
git branch -M main
git push -u origin main
    @staticmethod
    def storage_data(path):
        data = {}
        data_icon = lambda icon: f'data-icon='<span class="mif-{icon} mif-3x fg-teal">' [:-1]
        data_caption = lambda caption: f'data-caption="{caption}"'
        data_date = lambda date: f'data-date="{date}"'
        data_name = lambda name: f'data-name="{name}"'
        for root, dirs, files in os.walk(path, topdown=False):
            dirname = root.split('/')[-1]
            data[dirname] = {}
            if files:
                data[dirname]['files'] = {}
                for name in files:
                    file_path = os.path.join(root, name)
                    data[dirname]['files'][name] = {
                        'path': file_path,
                        'icon': data_icon(icon='file-empty'),
                        'caption': data_caption(caption=name),
                        'date': data_date(date=time.asctime(time.localtime(os.stat(file_path).st_atime))),
                        'name': data_name(name=name)}
            if dirs:
                data[dirname]['dirs'] = {}
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    data[dirname]['dirs'][name] = {
                        'path': dir_path,
                        'icon': data_icon(icon='folder'),
                        'caption': data_caption(caption=name[0].upper() + name[1:]),
                        'date': data_date(date=time.asctime(time.localtime(os.stat(dir_path).st_atime))),
                        'name': data_name(name=name)}
        directories = []
        if 'dirs' in list(data['storage'].keys()):
            for key in data['storage']['dirs'].keys():
                directories.append(
                    {'name': key, 'icon': 'mif-folder mif-3x fg-teal', 'caption': key[0].upper() + key[1:]})
        if 'files' in list(data['storage'].keys()):
            for key in data['storage']['files'].keys():
                directories.append(
                    {'name': key, 'icon': 'mif-file-empty mif-3x fg-teal', 'caption': key[0].upper() + key[1:]})
        return {'data': data, 'directories': directories}

    @staticmethod
    def build_storage_template(data):
        cls = 'container pl-2 pr-2 bg-dark fg-teal'
        table_data = {'role': '"listview"',
                      'view': '"table"',
                      'select-node': '"true"',
                      'structure': '\'{"date": true, "name": true}\''}
        attrs = ' '.join([f'data-{attr}={table_data[attr]}' for attr in table_data.keys()])
        rows = []
        if 'dirs' in list(data.keys()):
            for d in data['dirs'].keys():
                row_data = data['dirs'][d]
                rows.append(
                    f'<li {row_data["icon"]} {row_data["caption"]} {row_data["date"]} {row_data["name"]}></li>\n')
        if 'files' in list(data.keys()):
            for f in data['files'].keys():
                row_data = data['files'][f]
                rows.append(
                    f'<li {row_data["icon"]} {row_data["caption"]} {row_data["date"]} {row_data["name"]}></li>\n')
        content = ''.join(rows)
        return f'<ul class="{cls}" {attrs}>\n{content}</ul>'

    @staticmethod
    def upload_template(data):
        filetypes = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "mp4"}
        allowed_file = lambda filename: '.' in filename and filename.rsplit('.', 1)[1].lower() in filetypes
        template = lambda response: ''.join(
            ['<title>Upload File</title>\n',
             '<h1>Upload File</h1>\n',
             '<form method=post enctype=multipart/form-data>\n',
             '<input type=file name=file>\n',
             '<input type=submit value=Upload>\n',
             '</form>\n', f'<p>{response}</p>'])
        response = ''
        dir_name = data['request'].args.get('dirname')
        if dir_name is None:
            dir_name = './storage/'
        else:
            dir_name = f'./storage/{dir_name}/'
        file_req = data['request'].args.get('filename')
        send_file = data['send_file']
        if data['request'].method == 'POST':
            if 'file' not in data['request'].files:
                response = "No file part"
                return template(response=response)
            file = data['request'].files['file']
            filename = file.__dict__['filename']
            if filename == '':
                response = 'No selected file'
                return template(response=response)
            if allowed_file(filename):
                filename = secure_filename(filename)
                file.save(os.path.join('./storage', filename))
                response = f"{filename} uploaded"
                return template(response=response)
        elif file_req is not None:
            if file_req not in os.listdir(dir_name):
                response = f"filename with {file_req} not exist, please upload file before"
                return template(response=response)
            else:
                return send_file(dir_name + file_req, attachment_filename=file_req)
        else:
            return template(response)


@circuitalminds.route("/", methods=["GET", "POST"])
@circuitalminds.route("/<path>", methods=["GET", "POST"])
@circuitalminds.route("/<path>/<data>", methods=["GET", "POST"])
def home(path=None, data=None):
    dir_path = template_engine.path
    index = template_engine.index
    template = template_engine.template
    apps = template_engine.apps
    if path == 'desktop':
        if data in list(apps.keys()):
            if data == 'music_app':
                response = {'template': open(apps[data]['template']).read(),
                            'song_data': apps[data]['random_list']()}
                return jsonify(response)
        else:
            return render_template(index, dir_path=dir_path, template=template, apps=apps)
    elif path == 'storage':
        if data == 'media':
            video = request.args.get("v")
            image = request.args.get("img")
            if video is not None:
                return send_from_directory(f'{circuitalminds.config["storage"]}/{data}/videos/', video)
            else:
                return apps['upload']
        elif data == 'upload':
            data_upload = {'request': request, 'send_file': send_file}
            return template_engine.upload_template(data_upload)
    else:
        return redirect('https://circuitalmynds.github.io/')

class ScrapeTo:


    def __init__(self):
        from selenium import webdriver
        import geckodriver_autoinstaller
        geckodriver_autoinstaller.install()
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = lambda : webdriver.Firefox(options=options)
        self.yt_search = lambda video_title: f'https://www.youtube.com/results?search_query={video_title}'
        self.yt_watch = lambda video_id: f'https://www.youtube.com/watch?v={video_id}'

    def get_video_title(self, video_title):
        from time import sleep
        from bs4 import BeautifulSoup
        driver = self.driver()
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.get(self.yt_search(video_title=video_title))
        sleep(1)
        driver.set_window_size(S('Width'), S('Height'))
        sleep(1)
        video_data = driver.find_elements_by_id('video-title')
        song = {"name": video_data[0].get_attribute("title"), "url": video_data[0].get_attribute("href")}
        driver.close()
        return song

    def get_video_id(self, video_id):
        from time import sleep
        from bs4 import BeautifulSoup
        driver = self.driver()
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.get(self.yt_watch(video_id=video_id))
        sleep(1)
        driver.set_window_size(S('Width'), S('Height'))
        sleep(1)
        page = driver.page_source
        driver.close()
        return page


self.traffic = {"status": "ready"}

        self.api_workers = {"run_script": {
            "function": lambda in_console: {"output": subprocess.getoutput(f"python3 -c '{in_console}'")},
            "args": ["script"]},
            "get_cv": {
                "function": lambda: send_from_directory(
                    self.app_config['STORAGE'], filename="mycv.pdf"),
                "args": None},
            "socket_tasks": {
                "function": lambda args: self.yt_downloader(args=args),
                "args": ["video_url"]}}

        self.html_msg = lambda user, message: f"<h3>message by {user}: </h3><p>{message}</p>"
        url = "https://circuitalminds.herokuapp/your-name-here/your-message-here"
        user = "anonymous"
        message = f"Hello! Tell me something about you, what's your name? try {url}"
        self.messages = ["<title>API Messages</title>" + self.html_msg(user=user, message=message)]

    def bad_responses(self, cause):
        bad_responses = {"bad request": {"rejected": lambda data: f"{data} incomplete information in request"},
                         "bad query": {"rejected": lambda query: f"{query} not found or invalid",
                                       "invalid": lambda option: f"option {option} invalid",
                                       "null": lambda data: f"{data} not exists"}}
        return jsonify(bad_responses[cause])

    def yt_downloader(self, args):
        video_url = args["video_url"]
        if video_url is not None:
            if self.traffic["status"] == "busy":
                sleep(5)
            self.traffic["status"] = "busy"
            multitask.yt_downloader(video_url=video_url)
            self.traffic["status"] = "ready"
            return {"response": f"donwloading {video_url}"}
        else:
            return {"response": "video_url not founded"}

    def api_router(self, path, data):
        user = "anonymous"
        message = path
        if path is not None and data is not None:
            user = path
            message = data
        if message is not None:
            self.messages.append(self.html_msg(user=user, message=message))
        response = ""
        for msg in self.messages:
            response += msg
        return response

import requests
from bs4 import BeautifulSoup

language = "es"
url_wikipedia = f"https://{language}.wikipedia.org/wiki"


def get_genre(search):
    data = requests.get(f"{url_wikipedia}/{search}").text
    get_tables = BeautifulSoup(data, "html.parser").findAll("table")
    info_search = None
    list_info = None
    data_title = []
    for tab in get_tables:
        tab_class = ""
        _class = tab.get("class")
        if _class is None:
            break
        for j in range(len(_class)):
            if j == len(_class) - 1:
                tab_class += _class[j]
            else:
                tab_class += _class[j] + " "
        if tab_class == "infobox vcard plainlist" or tab_class == "infobox biography vcard":
            list_info = tab.findAll("tr")
            break
    if list_info is not None:
        for info in list_info:
            th_tag = info.find("th")
            title = str
            if th_tag is not None:
                title = th_tag.text
            if title == "Genres" or title == "Género":
                info_search = info
                break
    if info_search is not None:
        list_urls = info_search.findAll("li")
        if len(list_urls) == 0:
            list_urls = info_search.findAll("a")
        for url in list_urls:
            data_title.append(url.text)
    if len(data_title) > 0:
        return {"Genres": data_title}
    else:
        return "info not found"


def google_searc(artist):
    data = requests.get(f"https://www.google.com/search?q={artist}").text
    links = BeautifulSoup(data, "html.parser").findAll("a")
    search_wiki = str
    for link in links:
        url_search = link.get("href")
        if f"/url?q={url_wikipedia}" in url_search:
            search_data = url_search.split("&")[0].replace("/url?q=", "").split("/")[-1]
            search_wiki = requests.utils.unquote(search_data)
            break
    return search_wiki

'''




