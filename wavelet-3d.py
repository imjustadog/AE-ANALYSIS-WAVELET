#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pywt
import struct

cmap = plt.get_cmap('rainbow') # this may fail on older versions of matplotlib
#cmap.set_under(color='k', alpha=None)

fb = open("D://AE-wavelet//data//1", "rb")
x = 0
time = []
sst = []
while True:
    data = fb.read(4)
    if not data:
        break
    ch1, ch2 = struct.unpack('<HH', data)
    ch1 = (float(ch1) - 8192) / 8192 * 2.5
    ch2 = (float(ch2) - 8192) / 8192 * 2.5
    ch1 = float(ch1)
    ch2 = float(ch2)
    x = x + 1
    time.append(x * 0.0000001)
    sst.append(ch1)

dt = time[1]-time[0]

# Taken from http://nicolasfauchereau.github.io/climatecode/posts/wavelet-analysis-in-python/
wavelet = 'morl'
totalscale = 128
c = 2 * pywt.central_frequency(wavelet) * totalscale
a = np.arange(128, 0, -1)
scales = np.array(float(c)) / np.array(a)


[cfs,frequencies] = pywt.cwt(sst,scales,wavelet,dt)
power = (abs(cfs)) ** 2

time,frequencies = np.meshgrid(time,frequencies)
figure = plt.figure()
ax = Axes3D(figure)
ax.plot_surface(time, frequencies, power, rstride=1,cstride=1,cmap='rainbow')
plt.show()
