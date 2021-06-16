from python_resources import libs, utils
import sys


utils.get_info_resources(
    path='./python_resources/info.json', lib_names=list(libs.keys()), save_file=True
)


def get_resource(**args):
    return libs[args['lib']].__dict__[args['module']]()


def get_arguments():
    args = sys.argv[1:]
    if len(args) == 0:
        return None
    else:
        get_arg = lambda name: args[args.index(name) + 1]
        return {name: get_arg(name) for name in ['lib', 'module']}


if __name__ == '__main__':
    arguments = get_arguments()
    if arguments is None:
        pass
    else:
        resource = get_resource(**arguments)
