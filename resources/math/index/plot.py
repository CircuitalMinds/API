from numpy import meshgrid, min, max, linspace, pi, cos, zeros, sin
from matplotlib import rcParams, pyplot as plt
from random import sample
from json import load
from os.path import join
fdata = lambda filename: load(open(join("./settings", f"{filename}.json")))


class Color:
    by_name, palette = {}, {}
    def __init__(self):
        self.__dict__.update(fdata("colors"))
    hex_type = str
    rgb_type = int
    normal_type = float

    def get(self, *names):
        data = {}
        for name in names:
            if name in self.by_name:
                hex_data = self.by_name[name]["hex"]
                data[name] = {"hex": hex_data, "rgb": self.to_rgb(hex_data)}
        return data

    @classmethod
    def to_hex(cls, *values):
        hex_values = list(map(
            lambda c: "#" + ''.join([f"{ci:02x}" for ci in c]),
            [[int(vi * 255) for vi in v] if type(v[0]) == cls.normal_type else v for v in values]
        ))
        return hex_values[0] if len(hex_values) == 1 else hex_values

    @classmethod
    def to_rgb(cls, *values, normalized=True):
        fp = 1 / 255 if normalized else 1
        cn = (0, 2, 4)
        rgb_values = list(map(
            lambda c: tuple([fp * int(c[n + 1:n + 3], 16) for n in cn]),
            values
        ))
        return rgb_values[0] if len(rgb_values) == 1 else rgb_values

    def random(self, *data, sample_size=1):
        if data:
            return list(map(
                lambda c: self.to_rgb(c) if type(c[0]) == self.rgb_type else self.to_hex(c),
                data
            ))
        else:
            return self.get(*sample(list(self.by_name), sample_size))

class Layout:

    def __init__(self):
        self.params = rcParams
        self.update(**fdata("base"))
        self.models = fdata("layouts")

    def set_title(self, ax, data):
        ax.set_title(data)
        self.update()
        return ax

    def set_labels(self, ax, data):
        ax.set_title(data)
        self.update()
        return ax

    def update(self, **data):
        for k, v in data.items():
            if k in self.params:
                self.params.update(**{k: v})
        plt.tight_layout()
        return


class Graph:
    color = Color()
    layout = Layout()
    title = ""
    context = "2d"
    dataset = []
    colors = []
    gcf = {}


    def __init__(self, model=None):
        self.fig = plt.figure()
        if model in self.layout.models:
            self.__dict__.update(self.layout.models[model])
        self.ax = plt.axes(projection="3d") if self.context == "3d" else plt.axes()
        

    def add_dataset(self, *dataset, **params):
        line, = self.ax.plot(*dataset, **params)
        self.dataset.append(line)
        return

    def update(self, index, *dataset, **params):
        data = self.dataset[index]
        data.__dict__.update(**params)
        data.set_data(*dataset)
        self.dataset[index] = data
        return

    def show(self):
        self.layout.update()
        plt.show()
        return


def new_figure(context):
    from matplotlib import rcParams, pyplot as plt
    fig = plt.figure(**{"figsize": [15, 15], "frameon": False})
    ax = plt.axes(projection="3d") if context == "3d" else plt.axes()
    rcParams.update({"font.family": {"sans-serif": ["Helvetica"]}, "text.usetex": True})
    return plt, fig, ax

class Color:
    by_name, palette = get_settings("colors", "by_name", "palette")
    hex_type = str
    rgb_type = int
    normal_type = float

    def get(self, *names):
        data = {}
        for name in names:
            if name in self.by_name:
                hex_data = self.by_name[name]["hex"]
                data[name] = {"hex": hex_data, "rgb": self.to_rgb(hex_data)}
        return data

    @classmethod
    def to_hex(cls, *values):
        hex_values = list(map(
            lambda c: "#" + ''.join([f"{ci:02x}" for ci in c]),
            [[int(vi * 255) for vi in v] if type(v[0]) == cls.normal_type else v for v in values]
        ))
        return hex_values[0] if len(hex_values) == 1 else hex_values

    @classmethod
    def to_rgb(cls, *values, normalized=True):
        fp = 1 / 255 if normalized else 1
        cn = (0, 2, 4)
        rgb_values = list(map(
            lambda c: tuple([fp * int(c[n + 1:n + 3], 16) for n in cn]),
            values
        ))
        return rgb_values[0] if len(rgb_values) == 1 else rgb_values

    def random(self, *data, sample_size=1):
        if data:
            return list(map(
                lambda c: self.to_rgb(c) if type(c[0]) == self.rgb_type else self.to_hex(c),
                data
            ))
        else:
            return self.get(*sample(list(self.by_name), sample_size))


class Tex:

    @staticmethod
    def h_space(h):
        return r" \hspace{" + str(h) + r"mm} "

    @staticmethod
    def v_space(v):
        return r" \vspace{" + str(v) + r"mm} "

    @staticmethod
    def eq_style(string):
        return r" ".join(["$", r"\displaystyle", string, "$"])

    @classmethod
    def write(cls, *words, style="text"):
        data = r"".join([cls.h_space(2).join(word.split()) for word in words])
        if style == "text":
            return data
        elif style == "equation":
            return cls.eq_style(data)


class Style:
    background = "dark_background"
    fig_size = (10, 10)
    tight_layout = True
    font_size = 18
    color = "white"
    plot = dict(color="white", marker="*", markersize=1)
    surface = dict(cmap="Spectral_r", rstride=1, cstride=1)
    tick = type("tick", (), {"axis": ["x", "y", "z"], "style": dict(pad=5, labelsize=10)})()
    text = {
        "font.family": {"sans-serif": ["Helvetica"]},
        "text.usetex": True
    }
    label = type("label", (), {
        "style": {"fontsize": 18, "color": "teal"},
        "x": Tex.write("x"), "y": Tex.write("y"), "z": Tex.write("f(x, y)")
    })()
    title = type("title", (), {
        "style": {"fontsize": 18, "color": "teal", "pad": 10},
        "text": Tex.write("f(x) vs x")
    })()
    grid = dict(color='brown', linewidth=0.5)
    face_color = "gray"
    spines = {
        x: {'_position': 'zero', '_linewidth': 2.0} for x in ("left", "bottom", "right", "top")
    }
    fig_label = type("fig_text", (), {
        "w": 0.65, "h": 0.15, "text": Tex.write("y=f(x)"), "style": {"fontsize": 20, "color": "brown"}
    })()

    def create_object(self, ctx):
        from matplotlib import rcParams, pyplot as plt
        ax = None
        rcParams.update(self.text)
        plt.style.context(plt.style.use(self.background))
        if ctx == "2d":
            fig, ax = plt.subplots(figsize=self.fig_size, tight_layout=self.tight_layout)
            plt.gcf().text(self.fig_label.w, self.fig_label.h, self.fig_label.text, **self.fig_label.style)
            for k, v in self.spines.items():
                ax.spines[k].__dict__.update(v)
            ax.grid(**self.grid)
            ax.set_facecolor(self.face_color)
            ax.xaxis.set_ticks_position('bottom'), ax.yaxis.set_ticks_position('left')
        elif ctx == "3d":
            ax = plt.axes(projection="3d")
        return plt, ax



class Grapht(Style):

    def __init__(self, x, y, z=None):
        super(Grapht, self).__init__()
        self.x, self.y = x, y
        self.z = z if z.any() else []

    def plot2d(self):
        plt, ax = self.create_object("2d")
        x_lim = [min(self.x), max(self.x)]
        y_lim = [min(self.y), max(self.y)]
        for lim, val in ([ax.set_xlim, x_lim], [ax.set_ylim, y_lim]):
            lim(val[0], val[1])
        ax.plot(self.x, self.y, **self.plot)
        ax.set_xlabel(self.label.x, **self.label.style)
        ax.set_ylabel(self.label.y, **self.label.style)
        ax.set_title(self.title.text, **self.title.style)


    def plot3d(self):
        [X, Y], Z = meshgrid(self.x, self.y), self.z
        x_lim = [min(self.x), max(self.x)]
        y_lim = [min(self.y), max(self.y)]
        z_lim = [min(Z), max(Z)]
        plt, ax = self.create_object("3d")
        ax.plot_surface(X, Y, Z, **self.surface)
        for lim, val in ([ax.set_xlim, x_lim], [ax.set_ylim, y_lim], [ax.set_zlim, z_lim]):
            lim(val[0], val[1])
        ax.set_xlabel(self.label.x, **self.label.style)
        ax.set_ylabel(self.label.y, **self.label.style)
        ax.set_zlabel(self.label.z, **self.label.style)
        for xi in self.tick.axis:
            ax.tick_params(axis=xi, **self.tick.style)
        ax.view_init(45, -45)
        params = get_settings("params")
        for i in rcParams:
            if i in params:
                params[i] = rcParams[i].__repr__()
        print(params)




def test_graph():
    t = linspace(0, 1.0, 100)
    s = linspace(0, 1.0, 100)
    r, q = meshgrid(t, s)
    v = 0.5 * cos(pi * r) ** 2 + 0.5 * sin(pi * q) ** 2
    graph = Grapht(t, s, v)
    graph.plot2d()
    graph.plot3d()


t = linspace(0, 1.0, 100)
s = linspace(0, 1.0, 100)
rcParams.update(get_settings("params"))
figure = plt.figure()
plt.style.context(plt.style.use("dark_background"))
plt.plot(t, s)
plt.show()
"""""