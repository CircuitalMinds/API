import os
from werkzeug.utils import secure_filename
from flask import send_file, request, url_for, redirect, jsonify, Flask
from utils import FileHandlers



path = './storage'
join = lambda fpath: os.path.join(path, os.path.join(*fpath))
is_file = os.path.isfile
get_dirs = lambda fpath: {
    f: join([fpath, f]) if is_file(join([fpath, f])) else {
        d: join([fpath, f, d]) for d in os.listdir(join([fpath, f]))
    } for f in os.listdir(join([fpath]))
}
directory_data = {d: get_dirs(d) for d in os.listdir(path)}
info_data = FileHandlers.open_file(path='info.json')
info_data.update({"storage_data": directory_data})
FileHandlers.save_file(path='info.json', data=info_data)
is_allowed_file = lambda ext: any([ext in filetypes for filetypes in list(FileHandlers.allowed_files.values())])
is_post = lambda: request.method == 'POST'
response_file = lambda fpath: send_file(fpath, attachment_filename=fpath.split('/')[-1])

"""""
app = Flask(__name__)

def template(response_data):
    return '\n'.join([
        '<!DOCTYPE html>', '<html lang="en">',
        '<head>', '<meta charset="UTF-8">', '<title>Storage App</title>', '</head>',
        '<body>', '</body>', '\n'.join(response_data), '</html>'
    ])


def get_response(dir_name=''):
    if is_post():
        data = 'filename'
        return [
            '<h1>Upload File</h1>',
            '<form method=post enctype=multipart/form-data>',
            '<input type=file name=file>', '<input type=submit value=Upload>',
            '</form>',
            f'<p> {data} </p>'
        ]
    else:
        data = directory_data if dir_name == '' else directory_data[dir_name]
        response_data = []
        li = lambda fi: f'<li>{fi}</li>'
        ul = lambda ri: '\n'.join(['<ul>', '\n'.join(ri), '</ul>'])
        for dir_name in list(data):
            ei = [f'<p>{dir_name}</p>']
            for d in list(data[dir_name]):
                if type(data[dir_name][d]) == dict:
                    ei.extend([f'<p>{d}</p>', ul([li(f"{ki}: {di}") for ki, di in data[dir_name][d].items()])])
                else:
                    ei.append(li(f"{d}: {data[dir_name][d]}"))

            response_data.append(ul(ei))
        return template(response_data)

def handler(to_path, filename=None):
    if is_post():
            file = request.files['file']
            filename = file.__dict__['filename']
            if filename == '':
                response = 'No selected file'
                return template(response)
            elif is_allowed_file(ext=filename.split('.')[-1]):
                filename = secure_filename(filename=filename)
                file.save(join([to_path, filename]))
                response = f"{filename} uploaded to {to_path}"
                return template(response)
            else:
                response = f"filetype to {filename} not allowed"
                return template(response)
    else:
        if to_path is not None:
            if to_path in list(directory_data):
                if filename is not None:
                    if filename in list(directory_data[to_path]):
                        file_path = directory_data[filename]
                        return send_file(file_path, attachment_filename=filename)
                    else:
                        return jsonify(dict(Response=f'file with name={filename} not found in {to_path}'))
                else:
                    return jsonify(directory_data[to_path])
            else:
                return jsonify(dict(Response=f'directory with name={to_path} not found'))
        else:
            return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():
    return get_response()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
"""""