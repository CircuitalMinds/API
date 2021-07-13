import io
import random
from flask import Flask, Response, request
import numpy as np
from numpy.linalg import linalg as la
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
from matplotlib import rc
from mpmath import *
from matplotlib import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
rc('text', usetex=True)


class MplColorHelper:
    def __init__(self, cmap_name, start_val, stop_val):
        self.cmap_name = cmap_name
        self.cmap = plt.get_cmap(cmap_name)
        self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
        self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

    def get_rgb(self, val):
        return self.scalarMap.to_rgba(val)

# @app.route("/")
def index():
    num_x_points = int(request.args.get("num_x_points", 50))
    from flask import render_template
    return render_template("plotter.html", num_x_points=num_x_points)


# @app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_png(num_x_points=50):
    N, dt = 500 * num_x_points, 0.1
    z_r = np.zeros(N + 1)
    z_im = z_r.copy()
    fz = np.linspace(0.0, N * dt, N + 1)
    zf = lambda t: zeta(0.5 + fz[t] * j)
    z = [zf(t) for t in np.arange(len(fz))]
    for i in np.arange(len(z)):
        z_r[i], z_im[i] = float(z[i].real), float(z[i].imag)

    plt.show()
    fig = Figure(figsize=(20, 20), frameon=True)
    axis = fig.add_subplot(1, 1, 1)
    COL = MplColorHelper('Spectral_r', 7, 10)
    scat = axis.scatter(z_r, z_im, s=500, c=COL.get_rgb(z_r))
    axis.set_title('Well defined discrete colors')
    axis.set_facecolor('teal')
    axis.plot(z_r, z_im)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


# @app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


if __name__ == "__main__":
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
