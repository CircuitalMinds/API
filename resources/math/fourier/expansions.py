from numpy import cos, sin, pi, ceil, floor, tan, sqrt
from numpy import allclose, dot, concatenate, flipud, copy, sum
from numpy import arange, array, zeros, linspace, ones, column_stack, hstack, newaxis
from numpy import float64, real
from numpy.fft import fft, ifft
from scipy.linalg import toeplitz


class Base:
    fp = 2.0 * pi

    def __init__(self, xl, xr, dim):
        self.xl, self.xr, self.dim = xl, xr, dim
        self.dx = abs(xr - xl)
        self.scale = self.dx / (2.0 * pi)
        self.grid = xr + linspace(0, 2 * pi, dim) * self.scale
        self.basis = zeros([dim, dim])
        self._k, self.k = [
            arange(0, dim // 2, dtype=int),
            arange(1, dim // 2 + 1, dtype=int)
        ]
        self.basis[:, ::2] = cos(-self._k * self.grid[:, newaxis])
        self.basis[:, 1::2] = sin(self.k * self.grid[:, newaxis])


class Fourier(Base):
    resolvent = None

    def __init__(self, xl, xr, dim):
        super(Fourier, self).__init__(xl, xr, dim)

    def eval_resolvent(self, f):
        n, x = self.dim, self.grid        
        gz = dot(self.basis, f(x)) / n

        def g(*points):
            w = zeros(len(points), dtype=float64)
            for i, z in enumerate(points):
                zp = list(filter(lambda xi: allclose(z, xi), x))
                if zp:
                    w[i] = f(zp[0])
                else:
                    w[i] = sum(gz * f(z))
            return w[0] if len(w) == 1 else w
        self.resolvent = g
        return

    @staticmethod
    def transform(v):
        return fft(v)

    @staticmethod
    def inverse_transform(v_hat):
        return real(ifft(v_hat))

    def continuous_diff(self, n, *orders):
        w = 1j * array(
            self._k.tolist() + self.k.tolist(), dtype=complex
        ) * (self.dx / (self.dim * 2.0 * pi))
        if orders:
            dn = list(orders) + [n]

            def dy(x):
                yn = zeros(len(x[0]))
                for xi in x:
                    yn[:] = yn + xi
                return yn
            return lambda v: dy([self.inverse_transform(self.transform(v) * w ** i) if i > 0 else v for i in dn])
        else:
            return lambda v: self.inverse_transform(self.transform(v) * w ** n) if n > 0 else v

    def discrete_diff(self, n, *orders):
        dim = self.dim
        s = 0.5 * (dim - 1)
        h, n_1, n_2 = [2 * pi / dim, int(floor(s)), int(ceil(s))]

        def diff(m):
            if m == 0:
                col_1 = zeros(dim)
                col_1[0] = 1
                row_1 = copy(col_1)
            elif m == 1:
                col_1 = 0.5 * array([(-1) ** k for k in range(1, dim)], float)
                if dim % 2 == 0:
                    top_c = 1 / tan(arange(1, n_2 + 1) * h / 2)
                    col_1 = col_1 * hstack((top_c, - flipud(top_c[0:n_1])))
                    col_1 = hstack((0, col_1))
                else:
                    top_c = 1 / sin(arange(1, n_2 + 1) * h / 2)
                    col_1 = hstack((0, col_1 * hstack((top_c, flipud(top_c[0:n_1])))))
                row_1 = - col_1
            elif m == 2:
                col_1 = -0.5 * array([(-1) ** k for k in range(1, dim)], float)
                if dim % 2 == 0:
                    top_c = 1 / sin(arange(1, n_2 + 1) * h / 2) ** 2.
                    col_1 = col_1 * hstack((top_c, flipud(top_c[0:n_1])))
                    col_1 = hstack((- pi ** 2 / 3 / h ** 2 - 1 / 6, col_1))
                else:
                    top_c = 1 / tan(arange(1, n_2 + 1) * h / 2) / sin(arange(1, n_2 + 1) * h / 2)
                    col_1 = col_1 * hstack((top_c, - flipud(top_c[0:n_1])))
                    col_1 = hstack(([- pi ** 2 / 3 / h ** 2 + 1 / 12], col_1))
                row_1 = col_1
            else:
                nfo_1 = int(floor((dim - 1) / 2.0))
                nfo_2 = - dim / 2 * (m + 1) % 2 * ones((dim + 1) % 2)
                m_wave = 1j * concatenate((arange(nfo_1 + 1), nfo_2, arange(- nfo_1, 0)))
                col_1 = real(
                    ifft(
                        m_wave ** m * fft(hstack(([1], zeros(dim - 1))))
                    )
                )
                if m % 2 == 0:
                    row_1 = col_1
                else:
                    col_1 = hstack(([0], col_1[1:dim + 1]))
                    row_1 = - col_1
            return toeplitz(col_1, row_1)
        if orders:
            dn = list(orders) + [n]

            def dy(x):
                yn = zeros(len(x[0]))
                for xi in x:
                    yn[:] = yn + xi
                return yn

            return lambda v: dy([dot(diff(i), v) if i > 0 else v for i in dn])
        else:
            return lambda v: dot(diff(n), v) if n > 0 else v


class Chebyshev:

    def __init__(self, xl, xr, dim):
        self.xl, self.xr, self.dim = xl, xr, dim
        self.grid = - cos(
            pi * (array(range(0, dim)) + 0.5) / dim
        )
        self.c = (xl + xr) / 2.0
        self.m = (xr - xl) / 2.0
        self.fn = self.matrix()
        self.xn = (self.grid * (self.xr - self.xl) + (self.xr + self.xl)) / 2.0

    def approx(self, f):
        y = f(self.xn)
        c = 2.0 / self.dim * dot(y, self.fn)
        c[0] = c[0] / 2
        degree = len(c) - 1
        cn = array(c, ndmin=1)
        c, m = self.c, self.m

        def g(z):
            xa = array(z, copy=False, ndmin=1)
            u = array((xa - c) / m)
            tp = ones(len(u))
            w = cn[0] * tp
            v = None
            if degree > 0:
                w = w + u * cn[1]
                v = u
            for i in range(2, degree + 1):
                tn = 2 * u * v - tp
                tp = v
                v = tn
                w = w + v * cn[i]
            return w
        return g

    def matrix(self):
        t = column_stack((ones(len(self.grid)), self.grid))
        for i in range(2, self.dim + 1):
            x = 2 * self.grid * t[:, i - 1] - t[:, i - 2]
            t = column_stack((t, x))
        return t

    @staticmethod
    def transform(v):
        n = len(v) - 1
        if n == 0:
            w = 0.0  # only when N is even!
            return w
        x = cos(pi * arange(0, n + 1) / n)
        ii = arange(0, n)
        y = flipud(v[1:n])
        y = list(v) + list(y)
        u = real(fft(y))
        b = list(ii)
        b.append(0)
        b = b + list(arange(1 - n, 0))
        w_hat = 1j * array(b)
        w_hat = w_hat * u
        W = real(ifft(w_hat))
        w = zeros(n + 1)
        w[1:n] = -W[1:n] / sqrt(1 - x[1:n] ** 2)
        w[0] = sum(ii ** 2 * u[ii]) / n + 0.5 * n * u[n]
        w[n] = sum((-1) ** (ii + 1) * ii ** 2 * u[ii]) / n + 0.5 * (-1) ** (n + 1) * n * u[n]
        return w

    def diff(self, n, *orders):
        dfi = lambda v: self.transform(v)

        def df(v, m):
            dv = dfi(v)
            for i in range(m - 1):
                dv = dfi(dv)
            return dv
        if orders:
            dn = list(orders) + [n]
            return lambda v: [df(v, i) for i in dn]
        else:
            return lambda v: df(v, n)
