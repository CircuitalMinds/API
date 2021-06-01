import random
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
warnings.filterwarnings("ignore")
from mpmath import *
mp.dps = 10
mp.pretty = False
rc('text', usetex=True)


class Riemann:
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
        N = 2000
        T, dt = N // 10, 0.05
        z = [zeta(0.5 + tt * j) for tt in linspace(0.0, N * dt, N + 1)]
        self.config["z_re"] = np.array([float(zi.real) for zi in z])
        self.config["z_im"] = np.array([float(zi.imag) for zi in z])
        self.config["interval"], self.config["frames"], self.config["factor"] = T // 10, N // 10, N // T

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
            upper_bound = (i + 1) * factor  # up to what index to take the values
            re_i = re[:upper_bound]  # take the real
            im_i = im[:upper_bound]
            line.__dict__['_color'] = random_color()
            point.__dict__['_color'] = random_color()
            line.set_data(list(re_i), list(im_i))
            point.set_data([re[upper_bound - 1]], [im[upper_bound - 1]])
            return line, point
        anim = animation.FuncAnimation(fig, dynamic_function, frames=frames, interval=interval, blit=True)
        return anim


