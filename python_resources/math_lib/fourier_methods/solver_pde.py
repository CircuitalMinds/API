from numpy import pi, fft, dot, zeros, linspace
from scipy.integrate import odeint
import spectral_differentiation


class DiffEquation:
    arguments = dict(
        initial_condition=callable,
        space_dimension=str,
        time=linspace,
        boundary_conditions=list
    )

    def __init__(self, initial_condition, space_dimension, time, boundary_conditions: []):
        self.u0, self.n = initial_condition, space_dimension
        self.xl, self.xr = boundary_conditions
        self.x, self.t = zeros(space_dimension), time
        self.dt = self.t[1] - self.t[0]
        self.sol = zeros([len(time) + 1, self.n])
            
    def __repr__(self):
        return [f"< {arg} %r" % arg_type for arg, arg_type in DiffEquation.arguments.items()]

    def fourier_galerkin(self, equations):
        fourier_continuous = spectral_differentiation.fourier_continuous
        dx, T = [self.xr - self.xl, 2.0 * pi]
        scale_factor = T / dx
        waves = fourier_continuous(self.n)
        c_n, d_n = [], []
        [
            c_n.append(vi) if ki.startswith('c') else d_n.append(vi) for ki, vi in equations.items()
        ]
        fw = list(
            [c_n[i] * (1j * wi * scale_factor) ** d_n[i] for wi in waves] for i in range(len(d_n))
        )
        ode_system = lambda u, t: fft.ifft(
            sum((lambda u_hat: list(map(lambda wi: wi * u_hat, fw)))(fft.fft(u)))
        ).real
        self.sol = odeint(ode_system, self.u0(self.x), self.t)
        return self.sol

    def fourier_collocation(self, c_n, d_n):
        c_n = [c_n] if type(c_n) != list else c_n
        d_n = [d_n] if type(d_n) != list else d_n
        fourier_discrete = spectral_differentiation.fourier_discrete
        p_n, q_n = [], []
        [q_n.append([c_n[i], d_n[i]]) if type(d_n[i]) == list else p_n.append([c_n[i], d_n[i]])
            for i in range(len(d_n))]
        self.x, M_n = fourier_discrete(dimension=self.n, order_derivatives=[p_ni[1] for p_ni in p_n])
        dx, T = [self.xr - self.xl, 2.0 * pi]
        scale_factor = T / dx
        self.x = self.xl + self.x / scale_factor
        for i in range(len(p_n)):
            M_n[i] = p_n[i][0] * M_n[i] * scale_factor ** p_n[i][1]
        for i in range(len(q_n)):
            c_i, q_i = q_n[i][0], q_n[i][1]
            q_ni = fourier_discrete(dimension=self.n, order_derivatives=q_i)[1]
            M_n.append(c_i * dot(
                q_ni[0] * scale_factor ** q_i[0],
                q_ni[1] * scale_factor ** q_i[1]
            ))
        ode_system = lambda u, t: sum(list(map(lambda m_k: dot(m_k, u), M_n)))
        self.sol = odeint(ode_system, self.u0(self.x), self.t)
        return self.sol
