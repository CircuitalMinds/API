import numpy as np
from scipy import linalg as la


def interpolate(f, x):
    n, delta_x = len(x), x[-1] - x[0]
    x = x[-1] + np.linspace(0, 2 * np.pi, n) * delta_x / (2.0 * np.pi)
    _k, k = np.arange(0, n // 2, dtype=np.float64), np.arange(1, n // 2 + 1, dtype=np.float64)
    v = np.zeros((n, n))
    v[:, ::2] = np.cos(_k * x[:, np.newaxis])
    v[:, 1::2] = np.sin(k * x[:, np.newaxis])
    operator = la.solve(v, f(x))
    T_w = lambda zi: sum(la.eigvals(np.diag(operator + f(zi))).real) / n

    def collocation_point(z):
        points = np.zeros(len(z))
        for i in range(len(points)):
            x_test = [np.allclose(z[i], xi) for xi in x]
            if any(x_test):
                points[i] = x[x_test.index(True)]
            else:
                points[i] = T_w(z[i])
        return points

    return collocation_point