import yaml


git_options = dict(
    commit="git init && git add . && git commit -m 'auto'",
    push="git push",
    pull="git pull"
)
api = dict(
    localhost=dict(
        host="127.0.0.1", 
        port=6000,
        debug=True),
    production=dict(
        host='circuitalminds_api.herokuapp.com', 
        port=80, 
        debug=False
    )
)
app = dict(
  debug=True,
  host="127.0.0.1",
  port=7000
)
environment_config = dict(
    secret_key='circuitalminds',
    session_type='filesystem'
)


def save_file(option):
    filename = "./_config.yml"    
    config = dict(
        api=api[option],
        app=app,
        environment=environment_config
    )
    with open(filename, "w") as outfile:
        yaml.dump(config, outfile, default_flow_style=False)


def git_init(process):
    print(f"git process: {process} starting")
    print(git_options[process])
    print(f"git process: {process} finished")


opt = input("config app as localhost (1) or production (2) mode. (Enter) to pass: ")
if opt == '':
    pass
else:
    opt = int(opt)
    if opt == 1:
        save_file(option='localhost')
    elif opt == 2:
        save_file(option='production')

git_process = input('do git push (1) or pull (2) process. (Enter) to pass: ')
if git_process == '':
    pass
else:
    git_process = int(git_process)
    if git_process == 1:
        print(git_options['commit'])
        git_init(process='push')
    elif git_process == 2:
        print(git_options['commit'])
        git_init(process='pull')
