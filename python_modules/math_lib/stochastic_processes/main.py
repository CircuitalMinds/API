from scipy import stats
import numpy as np
import warnings
warnings.filterwarnings("ignore")


class RandomMotion:

    def __init__(self):
        args = {"brownian_motion":
                    {"args": dict(num_simulations=10, x_0=75.25, mu=0.23678, sigma=0.5392, N=2000, T=2),
                     "params": dict(num_simulations=10, x_0=75.25, mu=0.23678, sigma=0.5392, N=2000, T=2)},
                "geometric_motion":
                    {"args": dict(num_simulations=10, x_0=75.25, mu=0.23678, sigma=0.5392, N=2000, T=2),
                     "params": dict(num_simulations=10, x_0=75.25, mu=0.23678, sigma=0.5392, N=2000, T=2)}}
        self.config = {}

    def set_params(self):
        motion = self.config["motion"]
        if motion == "brownian":
            self.config["function"] = self.brownian_motion
        elif motion == "geometric":
            self.config["function"] = self.geometric_motion

    @staticmethod
    def brownian_motion(N, h, dt):
        random_increments = np.random.normal(0.0, 1.0 * h, N) * np.sqrt(dt)
        brownian_steps = np.cumsum(random_increments)
        brownian_steps = np.insert(brownian_steps, 0, 0.0)
        return brownian_steps, random_increments

    @staticmethod
    def random_walk(N):
        increments, p = np.array([1, -1]), 0.5
        random_increments = np.random.choice(increments, N, p)
        random_walk = np.cumsum(random_increments)
        return random_walk, random_increments

    @staticmethod
    def gaussian_increments(brownian_function, args, params):
        get_args = lambda keys: [args[key] for key in keys]
        get_params = lambda keys: [params[key] for key in keys]

        def simulation():
            N , T, h, dt, x, eps, t, iterations, ns, ts, hs, dts, u = get_args(
                keys=["N", "T", "h", "dt", "x"])
            eps, t, iterations, ns, ts, hs, dts, u = get_params(
                keys=["eps", "t", "iterations", "ns", "ts", "hs", "dts", "u"])
            t = int(np.floor((np.random.uniform(low=u + 0.01, high=1. * T - u) / T) * N))
            rand_val_t = np.zeros(iterations)
            rand_val_t_plus_u = np.zeros(iterations)
            for i in range(iterations):
                Xs, _ = brownian_function(ns, ts, hs)
                rand_val_t[i] = Xs[t]
                rand_val_t_plus_u[i] = Xs[t + int(u * ns / ts)]
            diff = rand_val_t_plus_u - rand_val_t
            return rand_val_t, rand_val_t_plus_u, diff, stats.normaltest(diff)
        return simulation

    @staticmethod
    def geometric_motion(brownian_function, args, params):
        get_args = lambda keys: [args[key] for key in keys]
        get_params = lambda keys: [params[key] for key in keys]

        def simulation():
            N, T, dt, iterations, min_value, max_value = get_args(
                keys=["N", "T", "dt", "iterations", "min_value", "max_value"])
            x_0, x_s, mu, sigma = get_params(
                keys=["x_0", "x_s", "mu", "sigma"])
            time_steps = np.linspace(0.0, N * dt, N + 1)
            for i in range(iterations):
                np.random.seed(42 + i)
                x_i = x_0 * np.exp(mu * time_steps + sigma * brownian_function(N, T, 1.0))
                x_i[0] = x_0
                min_value, max_value = np.minimum(min_value, np.min(x_i)), np.maximum(max_value, np.max(x_i))
                x_s.append(x_i)
            return x_s, min_value, max_value
        return simulation
