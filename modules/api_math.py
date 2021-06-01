import subprocess
import json


class MathApp:

    @staticmethod
    def get_info(module):
        info = subprocess.getoutput(f"cd ./math_tools && python3 -m main args_modules:{module}")
        parser_info = json.loads(json.dumps(info))
        return parser_info

    @staticmethod
    def run_script(module, args):
        _args = ""
        for k in list(args.keys()):
            _args += f"{k}:{args[k]} "
        _args = _args[::-1][1:][::-1]
        data = subprocess.getoutput(f"cd ./math_tools && python3 -m main args_modules:{module} {_args}")
        return data