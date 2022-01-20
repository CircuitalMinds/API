from numpy import linspace, zeros, complex64, float64
from plot import get_settings
from mpmath import zeta


class Zeta:
    settings = get_settings("models")[]

    def __init__(self, n):
        self.grid = 0.5 + linspace(0, 100, n, dtype=complex64) * 1j
        self.fz = self.grid.copy()
        self.set_values()

    def set_values(self):
        for i, zi in enumerate(self.grid):
            fi = zeta(zi)
            self.fz[i] = complex(float(fi.real), float(fi.imag))
        return

    @property
    def f_re(self):
        return self.fz.real

    @property
    def f_im(self):
        return self.fz.imag

    def create_animation(self):
        from matplotlib import pyplot as plt, rcParams
        from matplotlib.animation import FuncAnimation
        rcParams.update({'font.family': {'sans-serif': ['Helvetica']}, 'text.usetex': True})
        fig = plt.figure(figsize=(10, 10), frameon=False)
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

        ax.set_xticks(linspace(-3, 7, 10))
        ax.set_yticks(linspace(-3.5, 3.5, 10))
        ax.spines['right'].set_color('red')
        ax.spines['top'].set_color('red')
        colors_list = self.Figure.colors
        random_color = lambda: sample(colors_list, len(colors_list))[0]
        line, = ax.plot([], [], lw=1, color=colors_list[0])
        point, = ax.plot([], [], marker='o', markersize=16, color=colors_list[0])
        ax.set_title('Re vs. Im', color='black')
        ax.tick_params(labelcolor=colors_list[1], labelsize=8)
        title_txt = r'\textbf{$\displaystyle \mathcal{T} ( \mathcal{C}ircuital \otimes \mathcal{M}inds )$}'
        plt.gcf().text(
            0.7, 0.15, title_txt, fontsize=18, color=colors_list[3], fontfamily='sans-serif')
        plt.tight_layout()
        M = 10
        N = 2500
        T = N // M
        re = self.f_re
        im = self.f_im
        interval, frames, factor = T // M, N // M, M

        def frame(n):
            upper_bound = factor * n # up to what index to take the values
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
        data = FuncAnimation(fig, frame, frames=frames, interval=interval, blit=True)
        plt.show()
        return data

r_zeta = Zeta(2500)
r_zeta.create_animation()


