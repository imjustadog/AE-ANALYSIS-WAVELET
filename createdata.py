import struct
from math import *
fb=open("D://AE-wavelet//data//111","wb")
count = 0
t = -2.5
while True:
      if count < 200000 :
          t = 0
      else:
          t = 2.5 * (0.5 * sin(2 * pi * 15000 * count / 10000000) + 0.5 * sin(2 * pi * 30000 * count / 10000000))
          
      a = t / 2.5 * 8192 + 8192
      b = -1 * t / 2.5 * 8192 + 8192
      count = count + 1
      if count > 700000:
             break
      ch=struct.pack('<HH',a,b)
      fb.write(ch)

