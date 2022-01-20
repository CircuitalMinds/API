from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
warnings.filterwarnings("ignore")


def domain(x=-2, y=-2, w=4, h=4, density=200):
    re = np.linspace(x, x + w, w * density)
    im = np.linspace(y, y + h, h * density)
    return re, im


def constant(radius, angle):
    return complex(radius * np.cos(angle), radius * np.sin(angle))


def julia(re, im, c, threshold):
    w = np.zeros([len(re), len(im)])

    @jit
    def iterations(zi):
        for n in range(threshold):
            zi = zi ** 2 + c
            if abs(zi) > 4.0:
                return n
        return threshold - 1

    def vector(z):
        x, y = z
        for i in range(len(x)):
            for j in range(len(y)):
                w[i, j] = iterations(complex(x[i], y[j]))
        return w

    return vector([re, im])

def set_image(threshold=50, radius=0.7885, angle=np.pi/4):
    re, im = domain()
    c = constant(radius, angle)
    w = julia(re, im, c, threshold)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(w.T, interpolation="hamming", cmap='Spectral_r')
    plt.gcf().text(0.15, 0.1, 'by Alan', fontsize=18, fontfamily='sans-serif')
    plt.show()
    # plt.savefig('julia_Set.png', dpi=300, bbox_inches='tight')


def set_animation(threshold=20, radius=0.7885, frames=100, as_mp4=False):
    re, im = domain()
    cn = [constant(radius, ci) for ci in np.linspace(0, 2 * np.pi, frames)]
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()

    def animate(i):
        ax.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        w = julia(re, im, cn[i], threshold)
        img = ax.imshow(w.T, interpolation="hamming", cmap='Spectral_r')
        plt.gcf().text(0.15, 0.1, 'by Alan', fontsize=18, fontfamily='sans-serif')
        return [img]
    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
    if as_mp4:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        anim.save('julia_set.mp4', writer=writer)
    else:
        anim.save('julia_set.gif', writer='imagemagick')


set_image()