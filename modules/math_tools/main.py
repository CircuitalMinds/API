from FourierAnalysis import fourier
from FractalSimulations import fractal
from SpectralPDE import spectral_pde, spectral_fpk
from SpecialFunctions import riemann
from StochasticProcesses import random_motion
import sys
import os
import yaml
import numpy as np


class MathTools:
    modules = dict(fourier=fourier, fractal=fractal, random_motion=random_motion,
                   riemann=riemann, spectral_pde=spectral_pde, spectral_fpk=spectral_fpk)
    args_modules = {"fractal": {"args": dict(x_0=float, y_0=float, width=int, height=int, density=int),
                                "params": dict(frames=int, interval=int, threshold=int, r=float)},
                    "riemann": {"args": dict(N=int, T=float, dt=float, interval=int, frames=int, factor=int)}}

    def info(self):
        modules = list(MathTools.modules.keys())
        _info = ""
        for module in modules:
            _info += f'{module.__name__}: \n['
            for _key in list(module.__dict__.keys()):
                _info += f'    {_key}: {module.__dict__[_key]}\n'
            _info += '],\n'
        return _info
    
    def animations(self, option):
        anim = {"mandelbrot": fractal(select_fractal="mandelbrot").run_fractal,
                "julia": fractal(select_fractal="julia").run_fractal,
                "zeta_function": riemann().zeta_function}[option]
        anim().save(f"../static/animations/{option}.gif")


if __name__ == '__main__':
    data = sys.argv[1:]
    info = {"args_modules": MathTools.args_modules,
            "modules": MathTools.modules}
    args = {}
    for arg in data:
        k, v = arg.split(':')
        args[k] = v
    if "args_modules" in list(args.keys()):
        print(info["args_modules"][args["args_modules"]])
    elif "modules" in list(args.keys()):
        print(info["modules"][args["modules"]])
