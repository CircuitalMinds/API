from api_config import CircuitalMinds

circuitalminds = CircuitalMinds()
circuitalminds.__name__ = 'circuitalminds'
config = circuitalminds.settings['api']
config['port'] += 1
server = circuitalminds.get_server()
app = server.app


@app.route('/', methods=['GET', 'POST'])
def home():
    return server.modules.jsonify(dict(Response="hello"))

if __name__ == '__main__':
    import sys
    key, value = sys.argv[1].split('=')
    config[key] = value
    app.run(**config)
