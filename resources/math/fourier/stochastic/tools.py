from numpy import pi, sqrt, exp, array, zeros, inf
from math import factorial
from scipy.integrate import dblquad
from scipy.special import eval_hermitenorm


class Hermite:
    j = dict(
        N_4={
            "m": 7, "n1": 3, "seq": []
        },
        N_5={
            "m": 11, "n1": 4, "seq": []
        },
        N_6={
            "m": 18, "n1": 4, "seq": array([1, 3] + list(range(5, 7)) + [8] + list(range(11, 14))
                                              + [15, 17])
        },
        N_7={
            "m": 29, "n1": 4, "seq": array(list(range(1, 10)) + [11, 12, 13, 16, 18, 19, 23, 24, 25, 28,
                                                                    29])
        },
        N_8={
            "m": 60, "n1": 5, "seq": array(
                list(range(1, 10)) + [11, 12, 13, 16, 18, 19, 23, 24, 25, 28, 29, 31, 34, 35, 38, 39, 44, 48, 51, 55,
                                      59])
        },
        N_9={
            "m": 150, "n1": 5, "seq": array(
                list(range(1, 10)) + [11, 12, 13, 16, 18, 19, 23, 24, 25, 28, 29, 31, 34, 35, 38, 39, 44, 48, 51, 55,
                                      59, 63, 67, 70, 75, 81, 85, 89, 92, 95,
                                      99])
        }
    )
    def __init__(self, m):
        self.grades = zeros([m, m], dtype=int)
        for i, j, n in (
                [0, 0, 2], [0, 1, 1], [1, 1, 2],
                [0, 2, 1], [1, 2, 2], [2, 2, 1],
                [0, 3, 1], [1, 3, 2], [2, 3, 2]
        ): self.grades[i, j] = n

class Analysis:
    M = 0
    J = array([M, M])

    @staticmethod
    def measure(z):
        return exp(-0.5 * z ** 2) / sqrt(2.0 * pi)

    def evaluate(self, f, *params):
        return dblquad(
            f, -inf, inf,
            lambda x: self.measure(-inf),
            lambda x: self.measure(inf),
            args=params
        )

    @staticmethod
    def hermite(x, m):
        return eval_hermitenorm(m, x) / factorial(m + 1) ** 2

    @staticmethod
    def integ(f, Jlj):

        return lambda z: (1.0 / sqrt(2.0 * pi)) * exp(-0.5 * z ** 2)

    def distance(self, ux, uy):
        def fn(x, y, m):
            return abs(self.hermite(x, m) - self.hermite(y, m)) ** 2

        def gn(x, y, m):
            return abs(self.hermite(x, m)) ** 2

        norms = zeros(len(ux[:, 0]))
        for k in range(0, len(norms)):
            for j in range(0, self.M):
                for i in range(0, self.M):
                    prod1, prod2 = 1.0, 1.0
                    for l in range(0, self.M):
                        if self.J[l, j] > 0:
                            prod1 = prod1 * self.integ(fn, int(self.J[l, j]))
                            prod2 = prod2 * self.integ(gn, int(self.J[l, j]))
                    norms[k] = norms[k] + (
                            ux[k, self.J[i, j]] - uy[k, self.J[i, j]]) ** 2 * prod1 + ux[self.J[i, j]] ** 2 * prod2
        return norms