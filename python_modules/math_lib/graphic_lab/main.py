import numpy as np
import matplotlib
from matplotlib import pylab as plt
from matplotlib import rc
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
matplotlib.use('TKAgg', force=True)


class SetGraph:
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
