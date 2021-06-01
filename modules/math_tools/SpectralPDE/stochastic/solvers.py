from numpy import sin, pi, sqrt, exp, cos
import numpy as np
from math import factorial
import scipy.integrate as integrate
from scipy import special


hermite = special.eval_hermitenorm


class SetSystem:

    def __init__(self, u0, JNM, **params):
        self.u0 = u0
        self.nu = params['nu']
        self.x = params['x']
        self.t = params['t']
        self.N = params['N']

        # Hermite polynomials evaluation
        self.J = JNM().Js(self.N)
        self.M = len(self.J)
        self.EigValRe, self.EigValIm, self.EigVecRe, self.EigVecIm, self.U_1 = self.EigeF()
        self.H1 = self.SimulaX()

    def u02(self):
        """
        Function to calculate the constants of the system of ordinary differential equations given the initial condition

        Parameters
        ----------
        J : array; shape(M, M)
            Array containing the grades of the polynomials
        N : int; order max of the polynomials
        M : int; number of ODEs
        rulesX : array; polynomials of Hermite evaluated
        rulesW : array; weights of polynomials of Hermite evaluated
        LRules : array; length of rulesX array
        xSpace : array; discretized real space
        nu : array; Diffusion coefficient
        u0 : callable(x); initial condition function

        Returns
        -------
        ci: array, shape(M, len(xSpace))
            Array containing the constants of the system of ordinary differential equations

        """
        Lx, ci = len(self.x), np.zeros([self.M, Lx])
        for z in range(0, Lx):
            for i in range(0, self.M):
                sum2 = 0
                for k in range(0, self.M):
                    sum1 = 0
                    if self.J[k, i] > 0:
                        for y in range(0, self.LRules):
                            sum1 = sum1 + hermite(int(self.J[k, i]), self.rulesX[y]) * self.rulesX[y] * self.rulesW[y]
                    sum2 = sum2 + sum1 * self.u0(self.x[z]) * sqrt(2.0) / (sqrt(2.0 * self.nu) * pi * (k + 1))
                ci[i, z] = sum2
        return ci


    def Cnm(self):
        """
        Function to computes Matrix

        Parameters
        ----------
        J : array; shape(M, M)
        Array containing the grades of the polynomials
        M : int; max order polynomials
        rulesX : array; polynomials of Hermite evaluated
        rulesW : array; weigths of polynomials of Hermite evaluated
        LRules : array; length of rulesX array
        nu : array; Diffusion coefficient

        Returns
        -------
        Cnm: array, shape(len(t), len(y0))
        Array containing the value of y for each desired time in t,

        """
        Cnm, I4 = np.zeros([self.M, self.M]), self.integr4()
        for k in range(1, self.M):
            for i in range(1, self.M):
                I2 = self.integr2(self.J[:, k], self.J[:, i], k, i)
                sum1 = 0
                for j in range(0, self.M):
                    sum1 = sum1 + (j + 1) * sqrt(self.J[j, i]) * I4[j] * I2[j]
                Cnm[k, i] = sum1
        Cnm[0, 0] = pi * (-3.0) * I4[0]
        return Cnm

    def EigeF(self):

        """
        Function to computes eigenvalues and eigenvectors of the matrix A

        Parameters
        ----------
        J : array; shape(M, M)
            Array containing the grades of the polynomials
        N : int; order max of the polynomials
        M : int; number of ODEs
        rulesX : array; polynomials of Hermite evaluated
        rulesW : array; weights of polynomials of Hermite evaluated
        LRules : array; length of rulesX array
        xSpace : array; discretized real space
        nu : array; Diffusion coefficient
        u0 : callable(x); initial condition function

        Returns
        -------
        EigValRe: array, size M
            Array containing the real eigenvalues of matrix A
        EigValIm: array, size M
            Array containing the imaginary eigenvalues of matrix A
        EigVecRe: array, shape(M, M)
            Array containing the real eigenvectors of matrix A
        EigVecIm: array, shape(M, M)
            Array containing the imaginary eigenvectors of matrix A
        U_1: array, shape(M, len(xSpace))
            Array containing the ordinary differential equations system constants

        """
        Lamb1 = np.zeros([self.M, self.M])
        for i in range(0, self.M):
            sum1 = 0
            for j in range(0, self.M):
                sum1 = sum1 + self.J[j, i] * ((j + 1) ** 2) * pi ** 2
            Lamb1[i, i] = sum1 * self.nu
        ALambda1 = self.Cnm() - Lamb1
        Eig1 = np.linalg.eig(ALambda1)
        return Eig1[0].real, Eig1[0].imag, Eig1[1].real, Eig1[1].imag, self.u02()

    def SimulaX(self):
        """
        Function to simulate X.

        Parameters
        ----------
        J : array; shape([M, M])
            Array containing the grades of the polynomials
        M : int; number of ODEs
        xSpace : array; discretized real space
        nu : array; Diffusion coefficient
        u0 : callable(x); initial condition function

        Returns
        -------
        H : array, shape(M, len(xSpace))
            Array containing hermite polynomials evaluated to simulate real space

        """
        evalXSin = lambda x, k: sqrt(2.0 * self.nu) * k * pi * sqrt(2.0 / pi) * (self.u0(x)) * (sin(k * pi * x))
        Px = len(self.x)
        H = np.zeros([self.M, Px])
        for k in range(0, Px):
            for j in range(1, self.M):
                prod = 1.0
                for i in range(0, self.M):
                    if self.J[i, j] > 0:
                        x1 = integrate.quad(evalXSin, 0, 1, args=[k])[0]
                        prod = prod * hermite(int(self.J[i, j]), x1) * (1.0 / sqrt(factorial(self.J[i, j])))
                H[j, k] = prod
            x2 = self.x[k]
            H[0, k] = hermite(2, x2) - hermite(1, x2) + 1
        return H


class RunSimulation(SetSystem):

    def SimulaT(self, z, cons):
        """
        Function to simulate Time

        Parameters
        ----------
        tim : array; discretized time
        M : int; number of ODEs
        EigValRe : array, size M
            Array containing the real eigenvalues of matrix A
        EigValIm : array, size M
            Array containing the imaginary eigenvalues of matrix A
        EigVecRe : array, shape(M, M)
            Array containing the real eigenvectors of matrix A
        EigVecIm : array, shape(M, M)
            Array containing the imaginary eigenvectors of matrix A
        cons : array, shape(M, len(xSpace))
            Array containing the ordinary differential equations system constants

        Returns
        -------
        T : array, shape(len(tim), M)
            Array containing the solutions of each ODE for each zi on real space

        """

        T = np.zeros([len(self.t), self.M])
        for k in range(0, len(self.t)):
            for j in range(0, self.M):
                for i in range(0, self.M):
                    if (self.EigValIm[i] != 0 and i == 1) or (i > 1 and self.EigValIm[i] != - self.EigValIm[i - 1]):
                        T[k, j] = T[k, j]\
                                  + cons[i] * exp(self.EigValRe[i] * self.t[k] / pi ** 2) * (
                                self.EigVecRe[j, i] * cos(self.EigValIm[i] * self.t[k] / pi ** 2)
                                - self.EigVecIm[j, i] * sin(self.EigValIm[i] * self.t[k] / pi ** 2)
                                  )
                    elif self.EigValIm[i] == - self.EigValIm[i - 1]:
                        T[k, j] = T[k, j]\
                                  + cons[i] * exp(self.EigValRe[i] * self.t[k] / pi ** 2) * (
                                self.EigVecRe[j, i - 1] * sin(self.EigValIm[i - 1] * self.t[k] / pi ** 2)
                                + self.EigVecIm[j, i - 1] * cos(self.EigValIm[i - 1] * self.t[k] / pi ** 2)
                                  )
                    else:
                        T[k, j] = T[k, j]\
                                  + cons[i] * exp(self.EigValRe[i] * self.t[k] / pi ** 2) * self.EigVecRe[j, i]

        return np.dot(T, self.H1)[:, z]


    def SimulaTX(self):
        """
        Function to simulate Time-X.

        Parameters
        ----------
        xSpace : array; discretized real space

        Returns
        -------
        abs(Tx) : array, shape(len(tim), len(x))
            Array containing the solutions of partial equation

        """
        TX = np.zeros([len(self.t), len(self.x)])
        for zi in range(len(self.x)):
            TX[:, zi] = abs(self.SimulaT(zi, np.dot(np.linalg.inv(self.EigVecRe), self.U_1[:, zi])))

        return TX
