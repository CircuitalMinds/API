from matplotlib import pyplot as plt
from numpy import linspace
from json import load


def styles(name, default=True):
    if default:
        plt.style.use(['dark_background'])
    if name in plt.style.available:
        with plt.style.context(name) as plt_context:
            return plt_context


def latex(default=True, **options):
    from matplotlib import rcParams
    if default:
        rcParams.update({'font.family': {'sans-serif': ['Helvetica']}, 'text.usetex': True})
    rcParams.update(options)
    return rcParams


def zeta_style(title, labels):
    rc = latex()
    figure, ax = plt.subplots(figsize=(10, 10), frameon=False)
    ax = plt.axes(xlim=(-4, 7), ylim=(-3, 3))
    plt.title(title, fontsize=16, color='black')
    plt.xlabel(labels['x'], fontsize=15), plt.ylabel(labels['y'], fontsize=15)
    plt.gcf().text(0.55, 0.15, title, fontsize=20, color='white', fontfamily='sans-serif')
    ax.set_title('Re vs. Im', color='white')
    ax.grid(color='teal', linewidth=0.5), ax.tick_params(labelcolor='white', labelsize=8)
    ax.set_facecolor('black')
    ax.xaxis.set_ticks_position('bottom'), ax.yaxis.set_ticks_position('left')
    for i in ['left', 'bottom', 'right', 'top']:
        ax.spines[i].__dict__.update({'_position': 'zero', '_linewidth': 1.0})
    ax.set_xticks(linspace(-3, 7, 10))
    ax.set_yticks(linspace(-5, 5, 10))
    plt.tight_layout()
    return plt, figure, ax


def standard_context(dimension):
    from numpy import meshgrid, min, max

    def graph2d(x, y):
        plt.plot(x, y, (255, 255, 255))
        plt.grid()
        plt.xlabel('x', fontsize=15)
        plt.ylabel('y', fontsize=15)

    def graph3d(x, y, z):
        x, y = meshgrid(x, y)
        ax = plt.axes(projection="3d")
        ax.plot_surface(x, y, z, cmap='Spectral_r', rstride=1, cstride=1)
        ax.set_zlim(min(z), max(z))
        ax.set_xlabel(r'$x$', fontsize=25, labelpad=20)
        ax.set_ylabel(r'$y$', fontsize=25, labelpad=20)
        ax.set_zlabel(r'$f(x, y)$', fontsize=25, labelpad=30)
        ax.view_init(30, -80)
        ax.tick_params(axis='x', labelsize='25', pad=5)
        ax.tick_params(axis='y', labelsize='25', pad=5)
        ax.tick_params(axis='z', labelsize='25', pad=12)
        plt.tight_layout()
        plt.show()
    return {'2D': graph2d, '3D': graph3d}.get(dimension)
