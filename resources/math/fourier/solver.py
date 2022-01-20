from numpy import dot, real, ones, exp, linspace
from scipy.integrate import odeint
from spectral_operators import Fourier


class DiffEquation:

    def __init__(self, n, u0, space):
        self.dx = space[1] - space[0]
        self.n = n
        self.x, self.scale = Fourier.space_grid(space, n)
        self.f0 = u0(self.x)

    def discrete_system(self, linear=([], []), nonlinear=([], [], []), scheme='galerkin'):
        [am, bm], [cm, dm, em] = linear, nonlinear
        flux = ones(self.n)
        flux[0], flux[-1] = 0, 0
        dw = callable
        if scheme == 'galerkin':
            diff_x = Fourier.diff_continuous(self.dx, self.n)
            df = {di: lambda v: diff_x(v, di) for di in list(dict.fromkeys(bm + dm + em))}
            dw = lambda y, mi: df[mi](y)
        else:
            diff_x = Fourier.diff_discrete(self.dx, self.n)
            df = {di: diff_x(di) for di in list(dict.fromkeys(bm + dm + em))}
            dw = lambda y, mi: dot(y, df[mi]) * flux if mi > 0 else y
        linear_operator = lambda y: sum([am[i] * dw(y, bm[i]) for i in range(len(am))])
        nonlinear_operator = lambda y: sum([cm[i] * dw(y, dm[i]) * dw(y, em[i]) for i in range(len(cm))])
        odes = lambda g, s: linear_operator(g) + nonlinear_operator(g)
        return lambda time: odeint(odes, self.f0, time)
