import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
from matplotlib import cm
import matplotlib as mpl
warnings.filterwarnings("ignore")
from mpmath import *
mp.dps = 5
mp.pretty = False
from matplotlib import rc
rc('text', usetex=True)

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
        params = {"mandelbrot": dict(frames=25, interval=200, threshold=lambda step: round(1.15 * (step + 1)), r=None),
                  "julia": dict(frames=50, interval=200, threshold=lambda step: 50, r=0.7885)}
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


class CustomGraph:

    def __init__(self):
        self.plt = plt

    @staticmethod
    def rgb_convert(color):
        extreme_values = lambda c: 0 if c < 1 else 1
        converter = lambda c: c / 255 if 1 < c < 255 else extreme_values(c)
        return tuple([converter(c=ci) for ci in color])

    def animation_config(self):
        self.fig = self.plt.figure(figsize=(20, 20), frameon=True)
        ax = self.plt.axes(xlim=(-3, 7), ylim=(-3.5, 3.5))
        axis = self.fig.add_subplot(1, 1, 1)
        N, dt = 50 * 20, 0.1

        z_r = np.zeros(N + 1)
        z_im = z_r.copy()
        fz = np.linspace(0.0, N * dt, N + 1)
        zf = lambda t: zeta(0.5 + fz[t] * j)
        z = [zf(t) for t in np.arange(len(fz))]
        for i in np.arange(len(z)):
            z_r[i], z_im[i] = float(z[i].real), float(z[i].imag)
        COL = MplColorHelper('Spectral_r', 2, 8)

        axis.set_title('Well defined discrete colors')
        axis.set_facecolor('teal')
        #axis.plot(z_r, z_im)
        ax.tick_params(labelcolor=self.rgb_convert([76, 182, 182]), labelsize=8)
        ax.set_facecolor('black')
        ax.xaxis.set_ticks_position('bottom')

        ax.set_xticks(np.linspace(-3, 7, 10))
        ax.set_yticks(np.linspace(-3.5, 3.5, 10))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position('zero')
        ax.spines['left'].set_linewidth(1.0)
        ax.spines['bottom'].set_position('zero')
        ax.spines['bottom'].set_linewidth(1.0)
        ax.spines['right'].set_color(self.rgb_convert([153, 213, 213]))
        ax.spines['top'].set_color('red')
        """
        x = np.linspace(-np.pi, np.pi)
        y = np.exp(-0.05 * x**2)
        
        
        point_1, = ax.plot([], [], marker='*', markersize=16, color=self.rgb_convert([153, 213, 213]))
        """
        line, = ax.plot([], [], lw=1, color=self.rgb_convert([153, 213, 213]))
        point_0, = ax.plot([], [], marker='o', markersize=16, color=self.rgb_convert([153, 213, 213]))
        ax.set_title('Re vs. Im', color='white')
        title_txt = r'\textbf{$\displaystyle \mathcal{T} ( \mathcal{C}ircuital \otimes \mathcal{M}inds )$}'
        plt.gcf().text(
            0.5, 0.25, title_txt, fontsize=18, color=self.rgb_convert([153, 213, 213]), fontfamily='sans-serif')
        plt.tight_layout()
        scat = axis.scatter(z_r, z_im, s=50, c=COL.get_rgb(-z_r))
        l = ([], [])
        def anim_func(i):
            l[0].append(z_r[i])
            l[1].append(z_im[i])
            line.set_data(l)
            point_0.set_data([[z_r[i]], [z_im[i]]])
            return line, point_0

        anim = animation.FuncAnimation(self.fig, anim_func, frames=25, interval=450, blit=True)
        plt.show()
from numba import jit
N, dt = 50 * 20, 0.1
z_r = np.zeros(N + 1)
z_im = z_r.copy()
fz = np.linspace(0.0, N * dt, N + 1, dtype=np.complex)

fz = np.linspace(0.0, N * dt, N + 1, dtype=np.complex)
z = [zeta(0.5 + zeta(0.5 + fz[zi] * j) * j) for zi in np.arange(len(fz))]
@jit(nopython=True)
def f_zeta(N, dt):

    for i in np.arange(len(z)):
        z_r[i], z_im[i] = float(z[i].real), float(z[i].imag)

from numba import jit
import numpy as np
import time

x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace
go_fast(x)