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