import numpy as np
from numpy import linalg as la


class Fourier:
    """
    func - callable=[function to approximate]
    args - {"xl": float=[lower bound], "xr": float=[upper bound], "n": int=[order polynomial]}
    """
    modules = {"approximation": {"args": None}}

    def __init__(self, func, args):
        self.func = func
        self.data = {"args": args}

    def approximation(self):
        get_args = lambda keys: [self.data["args"][key] for key in keys]
        xl, xr, n = get_args(keys=["xl", "xr", "n"])
        x = xl + np.linspace(0, 2 * np.pi, n) * (xr - xl) / (2.0 * np.pi)
        _k, k = np.arange(0, n // 2, dtype=np.float64), np.arange(1, n // 2 + 1, dtype=np.float64)
        v = np.zeros((n, n))
        v[:, ::2] = np.cos(_k * x[:, np.newaxis])
        v[:, 1::2] = np.sin(k * x[:, np.newaxis])
        func_interpolated = self.func

        def select_point(zi):
            check = [np.allclose(zi, xi) for xi in x]
            if any(check):
                return func_interpolated(x[check.index(True)])
            else:
                return sum(la.eigvals(- np.diag(la.solve(v, func_interpolated(x)) - func_interpolated(zi))).real) / n
        self.data["approximation"] = select_point
