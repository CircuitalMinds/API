from numpy import linspace, complex64, max, min
from plot import get_settings, Tex
from mpmath import zeta
from matplotlib import pyplot as plt, rcParams
from matplotlib.animation import FuncAnimation


class Zeta:
    Fig = type("Fig", (), get_settings("models", "zeta"))

    def __init__(self, n):
        self.grid = 0.5 + linspace(0, 100, n, dtype=complex64) * 1j
        self.fz = self.grid.copy()
        self.set_values()
        self.Fig.axes.update({"xlim": set_limits(self.f_re), "ylim": set_limits(self.f_im)})

    def set_values(self):
        for i, zi in enumerate(self.grid):
            fi = zeta(zi)
            self.fz[i] = complex(float(fi.real), float(fi.imag))
        return

    def set_figure(self):
        rcParams.update(**self.Fig.params)
        fig = plt.figure(**self.Fig.view)
        axes = self.Fig.axes
        ax = plt.axes(**axes)
        ax.set_title(self.Fig.title["text"], **self.Fig.title["style"])
        ax.tick_params(**self.Fig.tick_params)
        ax.set_xlabel(Tex.write(self.Fig.label["axis"][0], style="equation"), **self.Fig.label["style"])
        ax.set_ylabel(Tex.write(self.Fig.label["axis"][1], style="equation"), **self.Fig.label["style"])
        ax.set_facecolor(self.Fig.facecolor)
        for k, v in self.Fig.spines.items():
            ax.spines[k].set_position(v["position"])
            ax.spines[k].set_linewidth(v["linewidth"])
            ax.spines[k].set_color(v["color"])
        ax.xaxis.set_ticks_position(self.Fig.axis["x"]["position"])
        ax.yaxis.set_ticks_position(self.Fig.axis["y"]["position"])
        ax.set_xticks(linspace(axes["xlim"][0], axes["xlim"][1], 10))
        ax.set_yticks(linspace(axes["ylim"][0], axes["ylim"][1], 10))
        line, = ax.plot([], [], **self.Fig.plot["line"])
        point, = ax.plot([], [], **self.Fig.plot["point"])
        subtitle = self.Fig.subtitle
        plt.gcf().text(
            subtitle["position"][0], subtitle["position"][1],
            Tex.write(subtitle["text"], style="equation"), **subtitle["style"]
        )
        line.set_data(self.f_re, self.f_im)
        point.set_data([self.f_re[-1]], [self.f_im[-1]])
        plt.tight_layout()
        plt.show()
        return

    def animation(self, fig, line, point, interval, frames, factor):
        re, im = [], []

        def frame(n):
            upper_bound = factor * n # up to what index to take the values
            re_i = re[:upper_bound]  # take the real
            im_i = im[:upper_bound]
            line.__dict__['_color'] = ''
            point.__dict__['_color'] = ''
            line.set_data(list(re_i), list(im_i))
            try:
                point.set_data([re[upper_bound - 1]], [im[upper_bound - 1]])
            except IndexError:
                print(upper_bound - 1)
                pass
            return line, point
        data = FuncAnimation(fig, frame, frames=frames, interval=interval, blit=True)
        return

    @property
    def f_re(self):
        return self.fz.real

    @property
    def f_im(self):
        return self.fz.imag
