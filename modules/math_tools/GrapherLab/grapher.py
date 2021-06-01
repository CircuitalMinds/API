import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)


class GraphViews:

    def __init__(self):
        self.config = {}

    def savefig(self, name):
        plt.savefig(name)

    def view_R2(self, x, z_t):
        plt.figure(figsize=(15, 15))
        plt.plot(x, z_t)
        plt.grid()
        plt.xlabel(r'\textit{$x$}', fontsize=15)
        plt.ylabel(r'\textbf{$\displaystyle \frac{1}{N} \sum_{n=0}^{N} \hat{u}_n (0) e^{inx} $}',
                         fontsize=15)
        self.savefig(name="./images/test.jpg")

    def view_R3(self, x, t, z):
        # Setting up Plot
        x, y = np.meshgrid(x, t)
        fig = plt.figure(figsize=(15, 15))
        ax = fig.gca(projection='3d')
        ax.plot_surface(x, y, z)
        surf = ax.plot_surface(x, y, z, cmap='Spectral_r', rstride=1, cstride=1)
        ax.set_zlim(np.min(z), np.max(z))
        ax.set_xlabel(r'$x$', fontsize=25, labelpad=20)
        ax.set_ylabel(r'$t$', fontsize=25, labelpad=20)
        ax.set_zlabel(r'$u(x, t)$', fontsize=25, labelpad=30)
        ax.view_init(30, -80)
        ax.tick_params(axis='x', labelsize='25', pad=5)
        ax.tick_params(axis='y', labelsize='25', pad=5)
        ax.tick_params(axis='z', labelsize='25', pad=12)
        plt.tight_layout()
        self.savefig(name="graph3D.jpg")

    @staticmethod
    def set_graph(ax, legend, type_graph):
        if type_graph == 'pointwise_max':
            ax[0].set_xlabel(r'\textit{$N$}', fontsize=15)
            ax[0].set_ylabel(r'\textbf{$\displaystyle \max_{t \in [0, T]} \| u - u_N \|_{L^2}$}',
                             fontsize=20)
            ax[1].set_xlabel(r'\textit{$N$}', fontsize=15)
            ax[1].set_ylabel(r'\textbf{$\displaystyle \max_{t \in [0, T]} | u - u_N |$}',
                             fontsize=20)
        else:
            ax[0].set_xlabel(r'$x$', fontsize=25, color='black')
            ax[0].set_ylabel(r'\textbf{$u_N$}',
                             fontsize=25, color='black')
            ax[1].set_xlabel(r'$x$', fontsize=25, color='black')
            ax[1].set_ylabel(r'\textbf{$| u - u_N |$}',
                             fontsize=25, color='black')
        ax[0].grid()
        ax[1].grid()
        rc_params = {'legend.fontsize': 25,
                     'legend.handlelength': 0.5}
        plt.rcParams.update(rc_params)
        ax[0].text(-0.1, 1.08, '(a)',
                   horizontalalignment='left', fontsize=25,
                   transform=ax[0].transAxes)
        ax[1].text(1.08, 1.08, '(b)',
                   horizontalalignment='left', fontsize=25,
                   transform=ax[0].transAxes)
        ax[0].legend(legend)
        ax[0].tick_params(axis='x', labelsize='25')
        ax[1].tick_params(axis='x', labelsize='25')
        ax[0].tick_params(axis='y', labelsize='25')
        ax[1].tick_params(axis='y', labelsize='25')

    def error_max(self, params, error, name='error_', *args):
        nu = params['nu']
        N = params['N']
        L2_distance = np.max(error['L2'])
        max_distance = np.max(error['L2'])

        colors = ['m-o', 'c-o', 'b-o', 'g-o', 'r-o']
        legend = [r'$\alpha$ = ' + str(nu[0])]
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].set_yscale('log')
        ax[0].plot(N, L2_distance, colors[0])
        ax[1].set_yscale('log')
        ax[1].plot(N, max_distance, colors[0])
        self.set_graph(ax, legend, 'pointwise_max')
        plt.tight_layout()
        self.savefig(name=f'{name}_nu={nu}.jpg')

    def error_time(self, params, exact, time, name='error_', *args):
        nu = params['nu']
        N = params['N']
        xL = params['xL']
        xR = params['xR']
        data = params['data']
        tdata = params['tdata']
        T = tdata.index(time)
        fig, ax = plt.subplots(1, 2, figsize=(15, 10))
        ax[0].set_xlim(xL, xR)
        ax[1].set_xlim(xL, xR)
        ax[0].set_xticks(np.linspace(xL, xR, 7))
        ax[1].set_xticks(np.linspace(xL, xR, 7))
        legend = [r'$u(x)$']
        colors = ['m--', 'c--', 'b--', 'g--', 'r--']
        legend = legend + ['N' + ' = ' + str(N)]
        ax[0].plot(data[T, :], exact[T, :], colors[0], linewidth=1.5)
        ax[1].semilogy(data[T, :], abs(data[T, :] - exact[T, :]), colors[0], linewidth=1.5)
        self.set_graph(ax, legend, 'pointwise_T')
        plt.tight_layout()
        self.savefig(name=f'{name}_nu={nu}_T={time}.jpg')