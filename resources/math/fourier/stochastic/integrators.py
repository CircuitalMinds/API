from numpy import sin, pi, sqrt, exp, cos
import numpy as np
from math import factorial
import scipy.integrate as integrate
from scipy import special
from tools import JNM


hermite = special.eval_hermitenorm
poly_hermite = np.polynomial.hermite_e.hermegauss(deg=200)
rulesX, rulesW, LRules = poly_hermite[0][::-1], poly_hermite[1], len(poly_hermite[0][::-1])


def integr1(N, M):
    """
    Function to calculate first type of integrals.

    Parameters
    ----------
    J : array; shape([M, M])
        Array containing the grades of the polynomials
    M : int; max order polynomials
    rulesX : array; polynomials of Hermite evaluated
    rulesW : array; weights of polynomials of Hermite evaluated
    LRules : array; length of rulesX array
    nu : float; Diffusion coefficient
    u0 : callable(x); initial condition function

    Returns
    -------
    intg : float, value of first type of integral

    """
    J = JNM().Js(N)
    intg = 0
    for k in range(0, LRules):
        prod = 1
        for i in range(0, M):
            if J[i, 0] > 0:
                prod = prod * hermite(int(J[i, 0]), rulesX[k])
        intg = intg + prod * rulesW[k]
    return intg, J


def integr2(Jm, Jn, r, i):
    """
    Function to calculate second type of integrals.
    Parameters
    ----------
    Jm : int; column m of matrix J
    Jn : int; column m of matrix J
    r : int; column index of matrix J
    i : int; column index of matrix J
    Returns
    -------
    intg : array, size M
        Array containing the values of second type of integral
    """
    sum2, prod = 0, 1.0
    Jn1, Jm1 = J[:, r], J[:, i]
    factor = lambda jn, jm: (1.0 / sqrt(factorial(int(Jn)))) * (1.0 / sqrt(factorial(int(Jm))))
    for o in range(0, M):
        sumparc = 0
        for l in range(0, LRules):
            x1 = rulesX[l]
            factor1 = factor(jn=Jn1[o], jm=Jm1[o])
            prod1 = hermite(int(Jn1[o]), x1) * hermite(int(Jm1[o]), x1) * factor1
            sumparc = sumparc + prod1 * rulesW[l] / (sqrt(2.0 * nu) * pi * (o + 1))
        prod = prod * sumparc
    for l in range(0, LRules):
        x2 = rulesX[l]
        factor2 = factor(jn=int(Jn[k]) - 1, jm=Jm[k])
        sum2 = sum2 + hermite(int(Jn[k]) - 1, x2) * hermite(int(Jm[k]), x2) * rulesW[l] * factor2
    return sum2 * prod


def integr3k(M):
    """
    Function to calculate third type of integrals.

    Parameters
    ----------
    M : int; size of individual timestep

    Returns
    -------
    int3 : array, size M
        Array containing the values of third type of integral

    """
    f = lambda x, i: sqrt(2.0) * sin(i * pi * x) * x
    int3 = np.zeros(M)
    for k in range(1, M + 1): int3[k - 1] = integrate.quad(f, 0, 1, args=[k])[0]
    return int3


def integr4(M, eqn):
    """
    Function to simulate T-X.

    Parameters
    ----------
    M : int; size of individual timestep

    Returns
    -------
    int4 : array, size M
        Array containing the values of fourth type of integral

    """
    f1 = lambda x, k, l: (l + 1) * pi * sin((k + 1) * pi * x) * cos((l + 1) * pi * x)
    f2 = lambda x, j, k, l: f1(x=x, k=l, l=k) * sin((j + 1) * pi * x)
    if eqn == "burgers":
        f = lambda x, j, k, l: 2.0 * (f1(x, k, l) + f2(x, j, k, l))
    else:
        f = lambda x, j, k, l: 2.0 * (sin((k + 1) * x) * sin((l + 1) * pi * x)) * sin((j + 1) * pi * x)
    int3, int4 = integr3k(M), np.zeros(M)
    for j in range(0, M):
        intM = np.zeros([M, M])
        for k in range(0, M):
            for l in range(0, M):
                integr = integrate.quad(f, 0, 1, args=[j, k, l])
                intM[l, k] = integr[0] * int3[l] * int3[k]
        int4[j] = sum(intM.sum(1))
        return int4
    else: return int3 - int4
