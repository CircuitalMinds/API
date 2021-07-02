import numpy as np
import matplotlib.pylab as plt
period = 2.0 * np.pi


def cn(time, n, y):
   c = y * np.exp(-1j * 2 * n * np.pi * time /period)
   return c.sum() / c.size

def f(x, Nh):
   f = np.array([2*cn(i, Nh, np.exp(1j*2*i*np.pi*x/ period)) for i in range(1,Nh+1)])
   return f.sum()

x = np.linspace(0, period)
print(np.fft.fftfreq(16) * 16)
