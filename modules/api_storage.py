import json
import os
import time
import requests
from werkzeug.utils import secure_filename


class StorageApp:

    def __init__(self, path):
        self.path = path
        self.home = self.get_home_directories(path=path)
        self.data = self.get_subdirectories(path=path)
        self.templates = self.build_storage_templates()
        self.save_to_json()

    def build_storage_templates(self):
        storage_templates = dict()
        for name in self.data.keys():
            storage_templates[name] = self.get_table(dir_data=self.data[name])
        return storage_templates

    def save_to_json(self):
        with open(f"{self.path}/storage_templates.json", "w") as outfile:
            json_file = json.dumps(self.templates, indent=4, sort_keys=True)
            outfile.write(json_file)
            outfile.close()

    @staticmethod
    def open_file_extension(filename):
        extensions = ['.mp4', '.json', '.py', '.png', '.gif']

    @staticmethod
    def get_home_directories(path):
        dirs = []
        dir_list = os.listdir(path)
        dir_list.remove('storage_templates.json')
        for d in os.listdir(path):
            dir_path = f'{path}/{d}'
            open_script = f"Apps.storage_app.open_script('{d}')"
            icon = f'mif-TYPE mif-3x fg-teal'
            if os.path.isfile(dir_path):
                icon = icon.replace('TYPE', 'file-empty')
            elif os.path.isdir(dir_path):
                icon = icon.replace('TYPE', 'folder')
            dirs.append(dict(name=d, open_script=open_script, icon=icon))
        return dirs

    @staticmethod
    def get_subdirectories(path):
        data = {}
        data_icon = lambda icon: f'''data-icon='<span class="mif-{icon} mif-3x fg-teal">' '''[:-1]
        data_caption = lambda caption: f'data-caption="{caption}"'
        data_date = lambda date: f'data-date="{date}"'
        data_name = lambda name: f'data-name="{name}"'
        data_onclick = lambda d_path, dirname: f'onclick=windowApps.storage_app("{d_path}/{requests.utils.quote(dirname)}")'
        for root, dirs, files in os.walk(path, topdown=False):
            d_path = root.split('/')[-1]
            data[d_path] = {}
            if files:
                data[d_path]['files'] = {}
                for name in files:
                    file_path = os.path.join(root, name)
                    data[d_path]['files'][name] = {
                        'path': file_path,
                        'onclick': data_onclick(d_path=d_path, dirname=name),
                        'icon': data_icon(icon='file-empty'),
                        'caption': data_caption(caption=name),
                        'date': data_date(date=time.asctime(time.localtime(os.stat(file_path).st_atime))),
                        'name': data_name(name=name)}
            if dirs:
                data[d_path]['dirs'] = {}
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    data[d_path]['dirs'][name] = {
                        'path': dir_path,
                        'onclick': data_onclick(d_path=d_path, dirname=name),
                        'icon': data_icon(icon='folder'),
                        'caption': data_caption(caption=name[0].upper() + name[1:]),
                        'date': data_date(date=time.asctime(time.localtime(os.stat(dir_path).st_atime))),
                        'name': data_name(name=name)}
        return data

    @staticmethod
    def get_table(dir_data):
        cls = 'container pl-2 pr-2 bg-dark fg-teal'
        table_data = {'role': '"listview"',
                      'view': '"table"',
                      'select-node': '"true"',
                      'structure': '\'{"date": true, "name": true}\''}
        attrs = ' '.join([f'data-{attr}={table_data[attr]}' for attr in table_data.keys()])
        rows = []
        if 'dirs' in list(dir_data.keys()):
            for d in dir_data['dirs'].keys():
                row_data = dir_data['dirs'][d]
                rows.append(
                    f'<li {row_data["onclick"]} {row_data["icon"]} {row_data["caption"]} {row_data["date"]} {row_data["name"]}></li>\n')
        if 'files' in list(dir_data.keys()):
            for f in dir_data['files'].keys():
                row_data = dir_data['files'][f]
                rows.append(
                    f'<li {row_data["onclick"]} {row_data["icon"]} {row_data["caption"]} {row_data["date"]} {row_data["name"]}></li>\n')
        content = ''.join(rows)
        return f'<ul id="storage-dir" class="{cls}" {attrs}>\n{content}</ul>'

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