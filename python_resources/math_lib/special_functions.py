import random
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
from matplotlib import cm
import matplotlib as mpl
from scipy import integrate
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
warnings.filterwarnings("ignore")
from mpmath import *
mp.dps = 10
mp.pretty = False
rc('text', usetex=True)


class MplColorHelper:

    def __init__(self, cmap_name, start_val, stop_val):
        self.cmap_name = cmap_name
        self.cmap = plt.get_cmap(cmap_name)
        self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
        self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

    def get_rgb(self, val):
        return self.scalarMap.to_rgba(val)


metric_color = MplColorHelper('Spectral_r', 1, 3)


class SpecialFunctions:
    """
    optional=[config] - {"args": dict(N=int, T=float, dt=float, interval=int, frames=int, factor=int)
    """
    modules = {"zeta_function": {"args": None}}

    def __init__(self, config=None):
        self.config = {}
        if config is None:
            self.default_settings()
        else:
            self.config.update(config)

    def default_settings(self):
        M = 10
        N = 100 * M
        dt = 0.05
        T = N // M
        z = [zeta(0.5 + tt * j) for tt in linspace(0.0, N * dt, N + 1)]
        self.config["z_re"] = np.array([float(zi.real) for zi in z])
        self.config["z_im"] = np.array([float(zi.imag) for zi in z])
        self.config["interval"], self.config["frames"], self.config["factor"] = T // M, N // M, M
        print(self.config["factor"])

    @staticmethod
    def animation_config():
        figure = plt.figure(figsize=(10, 10), frameon=False)
        ax = plt.axes(xlim=(-2.1, 6.1), ylim=(-3, 3))
        ax.tick_params(labelcolor='white', labelsize=12)
        ax.set_facecolor('teal')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position('zero')
        ax.spines['left'].set_linewidth(1.0)
        ax.spines['bottom'].set_position('zero')
        ax.spines['bottom'].set_linewidth(1.0)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        return figure, ax

    @staticmethod
    def rgb_convert(color):
        check_value = lambda data: 0 if data < 1 else 1
        converter = lambda data: data / 255 if 1 < data < 255 else check_value(data)
        return tuple([converter(data=data) for data in color])

    def zeta_function(self):
        get_params = lambda keys: [self.config[key] for key in keys]
        fig, ax = self.animation_config()
        ax.set_xticks(np.linspace(-3, 7, 10))
        ax.set_yticks(np.linspace(-3.5, 3.5, 10))
        ax.spines['right'].set_color(self.rgb_convert([153, 213, 213]))
        ax.spines['top'].set_color('red')
        colors_list = [(255, 255, 255), (153, 213, 213), (76, 182, 182), (0, 151, 151)]
        random_color = lambda: self.rgb_convert(color=colors_list[random.randint(0, 3)])
        line, = ax.plot([], [], lw=1, color=self.rgb_convert(color=colors_list[3]))
        point_0, = ax.plot([], [], marker='o', markersize=16, color=self.rgb_convert(color=colors_list[3]))
        point_1, = ax.plot([], [], marker='o', markersize=16, color=self.rgb_convert(color=colors_list[3]))
        ax.set_title('Re vs. Im', color='white')
        ax.tick_params(labelcolor=self.rgb_convert([76, 182, 182]), labelsize=8)
        title_txt = r'\textbf{$\displaystyle \mathcal{T} ( \mathcal{C}ircuital \otimes \mathcal{M}inds )$}'
        plt.gcf().text(
            0.7, 0.15, title_txt, fontsize=18, color=self.rgb_convert(colors_list[3]), fontfamily='sans-serif')
        plt.tight_layout()
        re, im, factor, frames, interval = get_params(keys=["z_re", "z_im", "factor", "frames", "interval"])

        def dynamic_function(i):
            upper_bound = factor * i  # up to what index to take the values
            re_i = re[:upper_bound]  # take the real
            im_i = im[:upper_bound]
            line.__dict__['_color'] = random_color()
            point_0.__dict__['_color'] = random_color()
            point_1.__dict__['_color'] = random_color()
            line.set_data(list(re_i), list(im_i))
            try:
                point_0.set_data([re[upper_bound - 1]], [im[upper_bound - 1]])
                point_1.set_data([- re[upper_bound - 1]], [- im[upper_bound - 1]])
            except IndexError:
                print(upper_bound - 1)
                pass
            return line, point_0, point_1
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
        self.fig = self.plt.figure(figsize=(10, 10), frameon=True)
        ax = self.plt.axes(xlim=(-3, 7), ylim=(-3.5, 3.5))

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
        x = np.linspace(-np.pi, np.pi)
        y = np.exp(-0.05 * x**2)
        line, = ax.plot([], [], lw=1, color=self.rgb_convert([153, 213, 213]))
        point_0, = ax.plot([], [], marker='o', markersize=16, color=self.rgb_convert([153, 213, 213]))
        point_1, = ax.plot([], [], marker='*', markersize=16, color=self.rgb_convert([153, 213, 213]))
        ax.set_title('Re vs. Im', color='white')
        title_txt = r'\textbf{$\displaystyle \mathcal{T} ( \mathcal{C}ircuital \otimes \mathcal{M}inds )$}'
        plt.gcf().text(
            0.5, 0.25, title_txt, fontsize=18, color=self.rgb_convert([153, 213, 213]), fontfamily='sans-serif')
        plt.tight_layout()
        l = ([], [])
        def anim_func(i):
            l[0].append(x[i])
            l[1].append(y[i])
            line.set_data(l)
            point_0.set_data([[x[i]], [y[i]]])
            point_1.set_data([[-x[i]], [-y[i]]])
            return line, point_0, point_1

        anim = animation.FuncAnimation(self.fig, anim_func, frames=50, interval=20, blit=True)
        plt.show()

    def lorenz(self):
        N_trajectories = 20

        def lorentz_deriv(v, t0, sigma=10., beta=8. / 3, rho=28.0):
            x, y, z = v
            return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

        np.random.seed(1)
        x0 = -15 + 30 * np.random.random((N_trajectories, 3))
        t = np.linspace(0, 4, 1000)
        x_t = np.asarray([integrate.odeint(lorentz_deriv, x0i, t)
                          for x0i in x0])
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1], projection='3d')
        ax.axis('off')
        colors = plt.cm.jet(np.linspace(0, 1, N_trajectories))

        lines = sum([ax.plot([], [], [], '-', c=c)
                     for c in colors], [])
        pts = sum([ax.plot([], [], [], 'o', c=c)
                   for c in colors], [])

        ax.set_xlim((-25, 25))
        ax.set_ylim((-35, 35))
        ax.set_zlim((5, 55))
        ax.view_init(30, 0)

        def init():
            for line, pt in zip(lines, pts):
                line.set_data([], [])
            return lines + pts

        def animate(i):
            i = (2 * i) % x_t.shape[1]
            for line, pt, xi in zip(lines, pts, x_t):
                x, y, z = xi[:i].T
                line.set_data(x, y)
                line.set_3d_properties(z)
                pt.set_data(x[-1:], y[-1:])
                pt.set_3d_properties(z[-1:])
            ax.view_init(30, 0.3 * i)
            fig.canvas.draw()
            return lines + pts

        anim = animation.FuncAnimation(
            fig, animate, init_func=init, frames=500, interval=30, blit=True
        )
        # anim.save('lorentz_attractor.mp4', fps=15, extra_args=['-vcodec', 'libx264'])
        plt.show()


import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib as mpl
from matplotlib import pylab as plt
from matplotlib import rc
from matplotlib.figure import Figure
import pyaudio
from mpmath import *
import warnings
warnings.filterwarnings("ignore")
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
import matplotlib.animation as animation
import warnings
warnings.filterwarnings("ignore")


def animation_config():
    figure = plt.figure(figsize=(10, 10), frameon=False)
    ax = plt.axes(xlim=(-2.1, 6.1), ylim=(-3, 3))
    ax.tick_params(labelcolor='white', labelsize=12)
    ax.set_facecolor('black')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_linewidth(1.0)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    return figure, ax

class MplColorHelper:

    def __init__(self, cmap_name, start_val, stop_val):
        self.cmap_name = cmap_name
        self.cmap = plt.get_cmap(cmap_name)
        self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
        self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

        x_0, y_0, width, height, density = -2.0, -1.5, 3, 3, 250
        self.z = dict(re=[], im=[])
        self.z["re"].extend(np.linspace(x_0, width, width * density))
        self.z["im"].extend(np.linspace(y_0, y_0 + height, height * density))

    def get_rgb(self, val):
        return self.scalarMap.to_rgba(val)



    @staticmethod
    def start_animation(z):
        frames, interval, threshold = 45, 120, lambda step: round(1.15 * (step + 1))
        def fractal_builder(z, c, threshold):
            for i in range(threshold):
                z = z ** 2 + c
                if abs(z) > 4.0:
                    return i
            return threshold - 1

        simulator = lambda i, j, step: fractal_builder(
            z=complex(0, 0),
            c=complex(z_re[i], z_im[j]),
            threshold=threshold(step)
        z_re, z_im = z["re"], z["im"]
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_xticks([])
        ax.set_yticks([])

        def dynamic_function(step):
            w = np.zeros([len(z), len(z)])
            for i in range(len(z_re)):
                for j in range(len(z_im)):
                    w[i, j] = simulator(i, j, step)
            img = ax.imshow(w.T, interpolation="hamming", cmap='twilight_shifted')

            return [img]
        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        return anim


    def tests(self):
        points = 32
        N, dt = 256 * points, 1.0 / points
        z_r = np.zeros(N + 1)
        z_im = z_r.copy()
        z = list(map(
            lambda ft: zeta(0.5 + ft * j), np.linspace(0.0, N * dt, N + 1)
        ))
        list(map(lambda i: [
            z_r.__setitem__(i, np.fft.fft(float(z[i]).real)),
            z_im.__setitem__(i, np.fft.fft(float(z[i]).imag))
        ], list(range(len(z)))))

        z = [zf(t) for t in np.arange(len(fz))]
        for i in np.arange(len(z)):
            z_r[i], z_im[i] = float(z[i].real), float(z[i].imag)

        fig = plt.figure(figsize=(20, 20), frameon=True)
        axis = fig.add_subplot(1, 1, 1)
        COL = MplColorHelper('Spectral_r', 1, 3)
        scat = axis.scatter(z_r, z_im, s=N, c=COL.get_rgb(np.sin(z_r * (2.0 * np.pi / max(z_r))) * np.exp(z_r ** 2)))
        axis.set_title('Well defined discrete colors')
        axis.set_facecolor('teal')
        axis.plot(z_r, z_im)
        plt.show()

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
    def start_animation(simulator, z, frames, interval):
        z_re, z_im = z["re"], z["im"]
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_xticks([])
        ax.set_yticks([])

        def dynamic_function(step):
            w = np.empty([len(z_re), len(z_im)])
            for i in range(len(z_re)):
                for j in range(len(z_im)):
                    w[i, j] = simulator(i, j, step)
            img = ax.imshow(w.T, interpolation="hamming", cmap='twilight_shifted')
            return [img]

        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        return anim

    def default_settings(self):
        M = 10
        N = 100 * M
        dt = 0.05
        T = N // M
        z = [zeta(0.5 + tt * j) for tt in linspace(0.0, N * dt, N + 1)]
        self.config["z_re"] = np.array([float(zi.real) for zi in z])
        self.config["z_im"] = np.array([float(zi.imag) for zi in z])
        self.config["interval"], self.config["frames"], self.config["factor"] = T // M, N // M, M
        print(self.config["factor"])

    @staticmethod
    def animation_config():
        figure = plt.figure(figsize=(10, 10), frameon=False)
        ax = plt.axes(xlim=(-2.1, 6.1), ylim=(-3, 3))
        ax.tick_params(labelcolor='white', labelsize=12)
        ax.set_facecolor('black')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position('zero')
        ax.spines['left'].set_linewidth(1.0)
        ax.spines['bottom'].set_position('zero')
        ax.spines['bottom'].set_linewidth(1.0)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        return figure, ax

    @staticmethod
    def rgb_convert(color):
        check_value = lambda data: 0 if data < 1 else 1
        converter = lambda data: data / 255 if 1 < data < 255 else check_value(data)
        return tuple([converter(data=data) for data in color])

    def zeta_function(self):
        get_params = lambda keys: [self.config[key] for key in keys]
        fig, ax = self.animation_config()
        colors_list = [(255, 255, 255), (153, 213, 213), (76, 182, 182), (0, 151, 151)]
        random_color = lambda: self.rgb_convert(color=colors_list[random.randint(0, 3)])
        line, = ax.plot([], [], lw=1, color=self.rgb_convert(color=colors_list[1]))
        point, = ax.plot([], [], marker='o', markersize=16, color=self.rgb_convert(color=colors_list[3]))
        ax.set_title('Re vs. Im', color='white')
        title_txt = r'\textbf{$\displaystyle \mathcal{T} ( \mathcal{C}ircuital \otimes \mathcal{M}inds )$}'
        plt.gcf().text(
            0.7, 0.15, title_txt, fontsize=18, color=self.rgb_convert(colors_list[3]), fontfamily='sans-serif')
        plt.tight_layout()
        re, im, factor, frames, interval = get_params(keys=["z_re", "z_im", "factor", "frames", "interval"])

        def dynamic_function(i):
            upper_bound = factor * i  # up to what index to take the values
            re_i = re[:upper_bound]  # take the real
            im_i = im[:upper_bound]
            line.__dict__['_color'] = random_color()
            point.__dict__['_color'] = random_color()
            line.set_data(list(re_i), list(im_i))
            try:
                point.set_data([re[upper_bound - 1]], [im[upper_bound - 1]])
            except IndexError:
                print(upper_bound - 1)
                pass
            return line, point

        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        return anim

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
