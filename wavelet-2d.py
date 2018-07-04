#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pywt
import struct

cmap = plt.get_cmap('gray') #cmap = plt.get_cmap('rainbow')
#cmap.set_under(color='k', alpha=None)

fb = open("D://AE-wavelet//data//1", "rb")
x = 0
max_value = 0
max_index = 0
data1 = []
while True:
    data = fb.read(4)
    if not data:
        break
    if x % 20 == 0:
        ch1, ch2 = struct.unpack('<HH', data)
        ch1 = (float(ch1) - 8192) / 8192 * 2.5
        ch2 = (float(ch2) - 8192) / 8192 * 2.5
        ch1 = float(ch1)
        ch2 = float(ch2)
        data1.append(ch1)
        if ch1 > max_value:
            max_value = ch1
            max_index = x / 20
    x = x + 1
	
sst1 = data1[max_index - 500 : max_index + 2500]
dt = 0.000002
time = range(len(sst1))

wavelet = 'morl'
totalscale = 1024
c = pywt.central_frequency(wavelet) * totalscale * 5
a = np.arange(1024, 0, -1)
scales = np.array(float(c)) / np.array(a)

[cfs1,frequencies1] = pywt.cwt(sst1,scales,wavelet,dt)
power1 = (abs(cfs1)) ** 2

for i in range(totalscale):
    power1[i] = power1[i] / scales[i]
	
ax = plt.gca()
cax = ax.contourf(time, frequencies1, power1,30,
            extend='both',cmap=cmap)
#cbar = plt.colorbar(cax)
ax.set_ylim(0, frequencies1[0])
plt.show()
