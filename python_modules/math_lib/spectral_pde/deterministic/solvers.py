from numpy import argmax, dot, fft, real, array
import sys
import yaml
import tools

spectral_operators = tools.SpectralOperators()
continuous_diff = spectral_operators.continuous_differentation
matrix_diff = spectral_operators.fourier_differentiation


def set_discrete_form(scheme, params):
    N, p, nu = params["order"], params["scale"], params["nu"]
    operator = {"matrix": {1: p * matrix_diff(N, 1), 2: p ** 2 * matrix_diff(N, 2)},
                "continuous": {1: lambda v: real(fft.ifft(
                    p * continuous_diff(discrete_size=N) * fft.fft(v))),
                               2: lambda v: real(fft.ifft(
                                   (p * continuous_diff(discrete_size=N)) ** 2 * fft.fft(v)))}}
    ik = lambda v: v * operator["continuous"][1](v)
    k2 = lambda v: nu * operator["continuous"][2](v)
    diff1 = lambda v: v * dot(operator["matrix"][1], v)
    diff2 = lambda v: nu * dot(operator["matrix"][2], v)
    return {"galerkin": lambda v: ik(v) + k2(v),
            "collocation": lambda v: diff1(v) + diff2(v)}[scheme]


def parser_data(arg):
    return array(yaml.load(arg, Loader=yaml.FullLoader))


def set_params(args):
    params = {}
    params["space"] = parser_data(arg=args["space"])
    params["u0"] = parser_data(arg=args["u0"])
    params["interval"] = parser_data(arg=args["interval"])
    params["dt"] = float(args["dt"])
    params["size_intervals"] = float(args["size_intervals"])
    params["nu"] = float(args["nu"])
    params["scale"] = float(args["scale"])
    params["order"] = int(args["order"])
    return args["scheme"], args["integration_method"], params


class EulerIntegrators:

    def __init__(self, scheme, integration_method, params):
        self.discrete_form = set_discrete_form(scheme=scheme, params=params)
        self.u0, self.time_interval, self.dt = params["u0"], params["interval"], params["dt"]
        self.data = {}
        self.time = self.time_interval[0]
        self.space = params["space"]
        for j in range(len(self.space)):
            self.data[self.space[j]] = {self.time: self.u0[j]}
        size = round((self.time_interval[1] - self.time_interval[0]) / self.dt) + 1
        self.steps = list(range(size))
        self.timer = lambda step: self.time_interval[0] + self.dt * self.steps[step]
        self.ode_system = lambda space_vector: self.discrete_form(v=space_vector)
        self.solver = {"explicit": self.explicit, "implicit": self.implicit}[integration_method]

    def step_function(self, integrator, time_step, space_vector):
         self.time, self.u0 = integrator(t=time_step, v=space_vector)
         for j in range(len(self.space)):
             self.data[self.space[j]].update({self.time: self.u0[j]})

    def explicit(self, time_step, out=False):
        integrator = lambda t, v: [self.timer(step=time_step), v + self.dt * self.ode_system(space_vector=v)]
        if out:
            return lambda vector: integrator(t=time_step, v=vector)
        else:
            try:
                self.step_function(integrator=integrator, time_step=time_step, space_vector=self.u0)
            except RuntimeError:
                pass

    def implicit(self, time_step):
        def integrator(t, vector):
            step_eval = self.explicit(time_step=t, out=True)
            error_function = lambda new_vector: argmax(
                new_vector - step_eval(vector=new_vector)[1]) > 1.0 * 10 ** (-8)
            new_vector = step_eval(vector=vector)
            while error_function(new_vector=new_vector[1]):
                new_vector = step_eval(vector=new_vector[1])
            return new_vector
        self.step_function(integrator=integrator, time_step=time_step, space_vector=self.u0)


if __name__ == '__main__':
    data = sys.argv[1:]
    length = len(data)
    keys = data[0:length - 1:2]
    values = data[1:length:2]
    args = {keys[j][1:]: values[j] for j in range(len(keys))}
    scheme, integration_method, params = set_params(args=args)
    integrator = EulerIntegrators(scheme=scheme, integration_method=integration_method, params=params)
    solver = integrator.solver
    for step in integrator.steps:
        solver(step)
    print(integrator.data)