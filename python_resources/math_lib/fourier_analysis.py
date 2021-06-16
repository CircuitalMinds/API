import numpy as np
from numpy.linalg import linalg as la


class FourierAnalysis:
    """
    func - callable=[function to approximate]
    args - {"xl": float=[lower bound], "xr": float=[upper bound], "n": int=[order polynomial]}
    """
    z = np.linspace(0, 2.0 * np.pi)
    func = np.cos
    xl = z[0]
    xr = z[1]
    n = len(z)
    
    def test(self):
        approx = self.approximation()
        return approx(self.z)

    def approximation(self):
        delta_x = self.xr - self.xl
        x = self.xl + np.linspace(0, 2 * np.pi, self.n) * delta_x / (2.0 * np.pi)
        _k, k = np.arange(0, self.n // 2, dtype=np.float64), np.arange(1, self.n // 2 + 1, dtype=np.float64)
        v = np.zeros((self.n, self.n))
        v[:, ::2] = np.cos(_k * x[:, np.newaxis])
        v[:, 1::2] = np.sin(k * x[:, np.newaxis])
        operator = la.solve(v, self.func(x))
        T_w = lambda zi: sum(la.eigvals(np.diag(operator + self.func(zi))).real) / self.n

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
