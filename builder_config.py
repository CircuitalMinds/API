import yaml


def build_config(option='deployment'):
    with open('_config.yml', "w") as outfile:
        yaml.dump(dict(
            host=dict(
                deployment="127.0.0.1", production="circuitalminds.herokuapp.com")[option],
            port=dict(
                deployment=5000, production=80)[option],
            debug=dict(
                deployment=True, production=False)[option],
            environment=dict(
                secret_key='circuitalminds', session_type='filesystem')
        ), outfile, default_flow_style=False)


opt = input("config app as deployment (1) or production (2) mode. (Enter) to pass: ")
if opt == '':
    pass
else:
    opt = int(opt)
    if opt == 1:
        build_config(option='deployment')
    elif opt == 2:
        build_config(option='production')
