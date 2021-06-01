import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
warnings.filterwarnings("ignore")


class Fractal:
    """
    select_fractal - str=[fractal name]
    optional=[config] - {"args": dict(x_0=float, y_0=float, width=int, height=int, density=int),
                         "params": dict(frames=int, interval=int, threshold=int, r=float)}
    """
    modules = {"simulator_config": {"args": None}}

    def __init__(self, select_fractal, config=None):
        args = {"mandelbrot": dict(x_0=-2.0, y_0=-1.5, width=3, height=3, density=250),
                "julia": dict(x_0=-2.0, y_0=-2.0, width=4, height=4, density=200)}
        params = {"mandelbrot": dict(frames=45, interval=120, threshold=lambda step: round(1.15 * (step + 1)), r=None),
                  "julia": dict(frames=100, interval=50, threshold=lambda step: 20, r=0.7885)}
        self.config = {"fractal": select_fractal,
                       "z": dict(re=[], im=[]),
                       "args": dict(x_0=float, y_0=float, width=int, height=int, density=int),
                       "params": dict(frames=int, interval=int, threshold=int, r=float)}
        if config is None:
            self.config["args"].update(args[select_fractal])
            self.config["params"].update(params[select_fractal])
        else:
            self.config.update(config)
        self.run_fractal = lambda: self.simulator_config()

    def get_info(self):
        info = "select_fractal:str, args:dict(["
        args, params = self.config["args"], self.config["params"]
        for arg in list(args.keys()):
            info += f'{arg}:{type(args[arg]).__name__},'
        info = info[::-1][1:][::-1] + "]), params:dict(["
        for param in list(params.keys()):
            info += f'{param}:{type(params[param]).__name__},'
        info = info[::-1][1:][::-1] + "])"
        return info

    def simulator_config(self):
        set_grid = lambda v, l, d: np.linspace(v, v + l, int(l * d))
        get_args = lambda keys: [self.config["args"][key] for key in keys]
        get_params = lambda keys: [self.config["params"][key] for key in keys]
        x_0, y_0, width, height, density = get_args(keys=["x_0", "y_0", "width", "height", "density"])
        frames, interval, threshold, r = get_params(keys=["frames", "interval", "threshold", "r"])
        self.config["z"]["re"].extend(set_grid(x_0, width, density))
        self.config["z"]["im"].extend(set_grid(y_0, height, density))
        simulator = None
        if self.config['fractal'] == "mandelbrot":
            simulator = lambda i, j, step: self.fractal_builder(
                z=complex(0, 0),
                c=complex(self.config["z"]["re"][i], self.config["z"]["im"][j]),
                threshold=threshold(step))
        elif self.config['fractal'] == "julia":
            self.config["a"] = np.linspace(0, 2.0 * np.pi, frames)
            simulator = lambda i, j, step: self.fractal_builder(
                z=complex(self.config["z"]["re"][i], self.config["z"]["im"][j]),
                c=complex(self.config["params"]["r"] * np.cos(self.config["a"][step]),
                          self.config["params"]["r"] * np.sin(self.config["a"][step])),
                threshold=threshold(step))
        return self.start_animation(simulator=simulator, z=self.config["z"], frames=frames, interval=interval)

    @staticmethod
    def fractal_builder(z, c, threshold):
        for i in range(threshold):
            z = z ** 2 + c
            if abs(z) > 4.0:
                return i
        return threshold - 1

    @staticmethod
    def start_animation(simulator, z, frames, interval):
        z_re, z_im = z["re"], z["im"]
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_xticks([], [])
        ax.set_yticks([], [])

        def dynamic_function(step):
            w = np.empty([len(z_re), len(z_im)])
            for i in range(len(z_re)):
                for j in range(len(z_im)):
                    w[i, j] = simulator(i, j, step)
            img = ax.imshow(w.T, interpolation="hamming", cmap='twilight_shifted')
            return [img]
        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        return anim



