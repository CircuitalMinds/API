import numpy as np
from scipy.linalg import toeplitz


def fourier_continuous(dimension):
    return np.array(
        list(
            range(- int(dimension / 2), int(dimension / 2))
        ), dtype=complex
    )


def chebyshev_continuous(real_space):
    """ Chebyshev differentiation via fft.
    Reference: Trefethen's 'Spectral Methods in MATLAB' book.
    """
    n = len(real_space) - 1
    if n == 0:
        w = 0.0  # only when N is even!
        return w
    x = np.cos(np.pi * np.arange(0, n + 1) / n)
    ii = np.arange(0, n)
    v = np.flipud(real_space[1:n])
    v = list(real_space) + list(v)
    u = np.real(np.fft.fft(v))
    b = list(ii)
    b.append(0)
    b = b + list(np.arange(1 - n, 0))
    w_hat = 1j * np.array(b)
    w_hat = w_hat * u
    W = np.real(np.fft.ifft(w_hat))
    w = np.zeros(n + 1)
    w[1:n] = -W[1:n] / np.sqrt(1 - x[1:n] ** 2)
    w[0] = sum(ii ** 2 * u[ii]) / n + 0.5 * n * u[n]
    w[n] = sum((-1) ** (ii + 1) * ii ** 2 * u[ii]) / n + 0.5 * (-1) ** (n + 1) * n * u[n]
    return w


def fourier_discrete(dimension, order_derivatives):
    """
    Fourier spectral differentiation.

    Spectral differentiation matrix on a grid with dimension equispaced points in [0,2pi)

    INPUT
    -----
    dimension: Size of differentiation matrix.
    order_derivative: Derivative required (non-negative integer)

    OUTPUT
    -------
    x: Equispaced points 0, 2pi/dimension, 4pi/dimension, ... , (dimension-1)2pi/dimension
    ddm: order_derivative'th order differentiation matrix

    Explicit formulas are used to compute the matrices for m=1 and 2.
    A discrete Fouier approach is employed for m>2. The program
    computes the first column and first row and then uses the
    toeplitz command to create the matrix.

    For order_derivative=1 and 2 the code implements a "flipping trick" to
    improve accuracy suggested by W. Don and A. Solomonoff in
    SIAM J. Sci. Comp. Vol. 6, pp. 1253--1268 (1994).
    The flipping trick is necesary since sin t can be computed to high
    relative precision when t is small whereas sin (pi-t) cannot.

    S.C. Reddy, J.A.C. Weideman 1998.  Corrected for MATLAB R13
    by JACW, April 2003.
    """
    # grid points
    x = 2 * np.pi * np.arange(dimension, dtype=float) / dimension
    # grid spacing
    h = 2 * np.pi / dimension
    n_1 = int(np.floor((dimension - 1) / 2.))
    n_2 = int(np.ceil((dimension - 1) / 2.))
    matrix_derivatives = []
    for order_derivative in order_derivatives:
        if order_derivative == 0:
            # compute first column of zeroth derivative matrix, which is identity
            col_1 = np.zeros(dimension)
            col_1[0] = 1
            row_1 = np.copy(col_1)
        elif order_derivative == 1:
            # compute first column of 1st derivative matrix
            col_1 = 0.5 * np.array([(-1) ** k for k in range(1, dimension)], float)
            if dimension % 2 == 0:
                top_c = 1 / np.tan(np.arange(1, n_2 + 1) * h / 2)
                col_1 = col_1 * np.hstack((top_c, -np.flipud(top_c[0:n_1])))
                col_1 = np.hstack((0, col_1))
            else:
                top_c = 1 / np.sin(np.arange(1, n_2 + 1) * h / 2)
                col1 = np.hstack((0, col_1 * np.hstack((top_c, np.flipud(top_c[0:n_1])))))
            # first row
            row_1 = - col_1
        elif order_derivative == 2:
            # compute first column of 1st derivative matrix
            col_1 = -0.5 * np.array([(-1) ** k for k in range(1, dimension)], float)
            if dimension % 2 == 0:
                top_c = 1 / np.sin(np.arange(1, n_2 + 1) * h / 2) ** 2.
                col_1 = col_1 * np.hstack((top_c, np.flipud(top_c[0:n_1])))
                col_1 = np.hstack((-np.pi ** 2 / 3 / h ** 2 - 1 / 6, col_1))
            else:
                top_c = 1 / np.tan(np.arange(1, n_2 + 1) * h / 2) / np.sin(np.arange(1, n_2 + 1) * h / 2)
                col_1 = col_1 * np.hstack((top_c, -np.flipud(top_c[0:n_1])))
                col_1 = np.hstack(([-np.pi ** 2 / 3 / h ** 2 + 1 / 12], col_1))
            # first row
            row_1 = col_1
        else:
            # employ FFT to compute 1st column of matrix for order_derivative > 2
            nfo_1 = int(np.floor((dimension - 1) / 2.0))
            nfo_2 = - dimension / 2 * (order_derivative + 1) % 2 * np.ones((dimension + 1) % 2)
            m_wave = 1j * np.concatenate((np.arange(nfo_1 + 1), nfo_2, np.arange(- nfo_1, 0)))
            col_1 = np.real(
                np.fft.ifft(
                    m_wave ** order_derivative * np.fft.fft(np.hstack(([1], np.zeros(dimension - 1))))
                )
            )
            if order_derivative % 2 == 0:
                row_1 = col_1
            else:
                col_1 = np.hstack(([0], col_1[1:dimension + 1]))
                row_1 = - col_1
        matrix_derivatives.append(toeplitz(col_1, row_1))

    return x, matrix_derivatives
