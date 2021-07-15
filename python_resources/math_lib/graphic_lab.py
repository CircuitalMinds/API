import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib as mpl
from matplotlib import pylab as plt
from matplotlib import rc
import random
import io
from mpmath import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
import warnings
warnings.filterwarnings("ignore")
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
matplotlib.use('TKAgg', force=True)


class MplColorHelper:
    def __init__(self, cmap_name, start_val, stop_val):
        self.cmap_name = cmap_name
        self.cmap = plt.get_cmap(cmap_name)
        self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
        self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

    def get_rgb(self, val):
        return self.scalarMap.to_rgba(val)


class GraphicLab:
    def __init__(self):
        self.plt = plt
        self.figure = self.plt.figure(figsize=(15, 15))

    @property
    def get_info(self):
        data = self.plt.__dict__
        get_data = lambda key: data[key].__dict__ if data[key].__dict__ != {} else data[key]
        check_key = lambda key: get_data(key) if key is not None and key in list(data.keys()) else 'invalid key'
        return lambda name=None: data if name is None else check_key(key=name)

    def set_graph2D(self, x, y):
        self.plt.plot(x, y)
        self.plt.grid()
        self.plt.xlabel('x', fontsize=15)
        self.plt.ylabel('y', fontsize=15)

    def set_graph3D(self, x, y, z):
        x, y = np.meshgrid(x, y)
        ax = self.plt.axes(projection="3d")
        ax.plot_surface(x, y, z, cmap='Spectral_r', rstride=1, cstride=1)
        ax.set_zlim(np.min(z), np.max(z))
        ax.set_xlabel(r'$x$', fontsize=25, labelpad=20)
        ax.set_ylabel(r'$y$', fontsize=25, labelpad=20)
        ax.set_zlabel(r'$f(x, y)$', fontsize=25, labelpad=30)
        ax.view_init(30, -80)
        ax.tick_params(axis='x', labelsize='25', pad=5)
        ax.tick_params(axis='y', labelsize='25', pad=5)
        ax.tick_params(axis='z', labelsize='25', pad=12)
        self.plt.tight_layout()
        self.plt.show()


class AppViews:

    def __init__(self, response):
        self.response = response

    def plot_svg(self, num_x_points=50):
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        x_points = range(num_x_points)
        axis.plot(x_points, [random.randint(1, 30) for x in x_points])
        output = io.BytesIO()
        FigureCanvasSVG(fig).print_svg(output)
        return self.response(output.getvalue(), mimetype="image/svg+xml")

    def plot_png(self, num_x_points=50):
        N, dt = 500 * num_x_points, 0.1
        x = np.linspace(0, dt * N, N)
        y = np.cos(x)
        fig = Figure(figsize=(20, 20), frameon=True)
        axis = fig.add_subplot(1, 1, 1)
        COL = MplColorHelper('Spectral_r', 7, 10)
        scat = axis.scatter(x, y, s=500, c=COL.get_rgb(y))
        axis.set_title('Well defined discrete colors')
        axis.set_facecolor('teal')
        axis.plot(x, y)
        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        return self.response(output.getvalue(), mimetype="image/png+xml")


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
from matplotlib import cm
import matplotlib as mpl
warnings.filterwarnings("ignore")


class MplColorHelper:

    def __init__(self, cmap_name, start_val, stop_val):
        self.cmap_name = cmap_name
        self.cmap = plt.get_cmap(cmap_name)
        self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
        self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

    def get_rgb(self, val):
        return self.scalarMap.to_rgba(val)


class FractalSimulations:
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
        fig = plt.figure(figsize=(10, 10), frameon=False)
        ax = plt.axes()
        ax.set_xticks([])
        ax.set_yticks([])

        def dynamic_function(step):
            w = np.empty([len(z_re), len(z_im)])
            for i in range(len(z_re)):
                for j in range(len(z_im)):
                    w[i, j] = simulator(i, j, step)
            img = ax.imshow(w.T, interpolation="hamming", cmap='Spectral_r')
            return [img]
        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        plt.show()
        return anim


class Plotter:

    @staticmethod
    def plot_png(data, Response):
        output = io.BytesIO()
        FigureCanvasSVG(data).print_svg(output)
        return Response(output.getvalue(), mimetype="image/svg+xml")

    @staticmethod
    def plot_svg(data, Response):
        output = io.BytesIO()
        FigureCanvasSVG(data).print_svg(output)
        return Response(output.getvalue(), mimetype="image/svg+xml")