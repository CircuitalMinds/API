from expansions import Fourier, pi, cos


class Galerkin(Fourier):

    def operator(self, f, dn):
        if len(dn) > 1:
            return self.continuous_diff(dn[0], *dn[1:])(f(self.grid))
        else:
            return self.continuous_diff(dn[0])(f(self.grid))

