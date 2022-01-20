class Match:

    @staticmethod
    def tester(x, y):
        ux, uy = ["".join(s.split()) for s in (x, y)]
        u_xy = ux + uy
        u, v = [
            {xi for xi in ux if xi in u_xy},
            {yi for yi in uy if yi in u_xy}
        ]
        w = u.union(v)
        x_w, y_w = [], []
        for wi in w:
            x_w.append(1) if wi in u else x_w.append(0)
            y_w.append(1) if wi in v else y_w.append(0)
        xs, ys = sum(x_w), sum(y_w)
        if xs != 0 and ys != 0:
            return sum([
                float(x_w[n]) * float(y_w[n]) for n in range(len(w))
            ]) / float(xs * ys) ** 0.5
        else:
            return 0.0

def tester(x, y):
    not_allow = [",", ".", "", " "]
    ux = {xi for xi in x.casefold() if xi not in not_allow}
    uy = {yi for yi in y.casefold() if yi not in not_allow}
    print(ux, uy)
    w = ux.intersection(uy)
    print(w)
    x_w, y_w = [1. if wi in w else 0. for wi in ux], [1. if wi in w else 0. for wi in uy]
    print(x_w, y_w)
    s_xy = (sum(x_w) * sum(y_w)) ** 0.5
    if s_xy != 0:
        p_xy = sum(xi * yi for xi, yi in zip(x_w, y_w))
        return p_xy / s_xy
    else:
        return 0.0
x = "Those weaving oboes are so satisfying, and the harps..  the whole thing is kinda of indescribable"
y = "harps"
print(tester( y,x))