import subprocess
import yaml
from numpy import pi, exp


class SolverPDE:
    arguments = ["initial_condition", "spectral_scheme", "order_polynomial", "integration_method", "nu",
                 "initial_time", "final_time", "time_size_intervals", "space_bound_left", "space_bound_right"]
    types = ["callable", "str", "int", "str", "float",
             "float", "float", "float", "float", "float"]
    test = dict(initial_condition=lambda x: exp(-0.01 * x ** 2), nu=0.1, spectral_scheme="collocation",
                order_polynomial=64, integration_method="explicit", initial_time=0.0, final_time=100.0,
                time_size_intervals=0.1, space_bound_left=-60, space_bound_right=60.0)

    def __init__(self, args):
        self.scheme, self.integration_method, self.params = self.set_params(data=args)

    def __repr__(self):
        return [f"< {SolverPDE.arguments[j]} %r" % SolverPDE.types[j] for j in range(len(SolverPDE.arguments))]

    def set_params(self, data):
        args = dict.fromkeys(SolverPDE.arguments)
        args.update({key: data[key] for key in list(args.keys())})
        return args["spectral_scheme"], args["integration_method"], self.set_system(args=args)

    @staticmethod
    def set_system(args):
        # setting time
        time_interval = [args["initial_time"], args["final_time"]]
        # setting space
        x = [args["space_bound_left"], args["space_bound_right"]]
        N = args["order_polynomial"]
        h = 2.0 * pi / N
        waves = list(range(- int(N / 2), int(N / 2)))[::-1]
        scale_factor = 2.0 * pi / (x[0] - x[1])
        space = [wave * h / scale_factor for wave in waves]
        u0 = [args["initial_condition"](space[j]) for j in range(len(space))]
        return {"space": space, "size_intervals": h, "scale": scale_factor,
                "order": N, "nu": args["nu"], "u0": u0,
                "interval": time_interval, "dt": args["time_size_intervals"]}

    @staticmethod
    def parser_data(string_data):
        return yaml.load(string_data, Loader=yaml.FullLoader)

    def init_solver(self):
        location = subprocess.getoutput("pwd").split("/")[-1]
        path = None
        if location == "deterministic":
            path = "./"
        else:
            path = "./math_tools/pySpectralPDE/deterministic"
        go_path = f"cd {path}"
        config = f"-scheme {self.scheme} -integration_method {self.integration_method}"
        for key in list(self.params.keys()):
            config += f" -{key} '{self.params[key]}'"
        command = f"{go_path} && python3 -m solvers {config}"
        v = self.parser_data(string_data=subprocess.getoutput(command))
        x = list(v.keys())
        t = list(v[x[0]].keys())
        z = lambda i, j: [x[i], t[j], v[x[i]][t[j]]]
        return z

    @staticmethod
    def save_data(data, name):
        with open(name + ".yml", "w") as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
