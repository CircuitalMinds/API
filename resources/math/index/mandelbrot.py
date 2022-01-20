from numba import jit, guvectorize, complex128, int64
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from layouts import latex
import warnings
warnings.filterwarnings("ignore")


def mandelbrot_set(xmin=-2, xmax=1, ymin=-1.5, ymax=1.5, npts=1024):
    rc = latex()
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()

    @jit
    def mandelbrot_iteration(c, maxiter):
        z = 0
        for n in range(maxiter):
            z = z ** 2 + c
            if z.real * z.real + z.imag * z.imag > 4:
                return n
        return maxiter

    @guvectorize([(complex128[:], int64[:], int64[:])], '(n), () -> (n)',
                 target='parallel')
    def mandelbrot(c, itermax, output):
        nitermax = itermax[0]
        for i in range(c.shape[0]):
            output[i] = mandelbrot_iteration(c[i], nitermax)

    def animate(i):
        ax.clear(), ax.set_xticks([]), ax.set_yticks([])
        cy, cx = np.ogrid[ymin:ymax:npts * 1j, xmin:xmax:npts * 1j]
        data = mandelbrot(cx + cy * 1j, round(1.15 ** (i + 1))) * - 1.0
        img = ax.imshow(data, interpolation="hamming", cmap='Spectral')
        plt.gcf().text(0.65, 0.15,
                       r'$ \displaystyle \mathcal{C} ircuital \hspace{1mm} \mathcal{M} inds. $',
                       fontsize=22, fontfamily='sans-serif')
        return [img]

    anim = animation.FuncAnimation(fig, animate, frames=45, interval=150, blit=True)
    anim.save('mandelbrot.gif', writer='imagemagick')
