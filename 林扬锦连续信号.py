import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,200)
f1 = np.exp(-3*t)
f2 = np.sin(4*np.pi*t)
plt.subplot(321)
plt.ylim(-1,2)
plt.plot(t,f1)
plt.subplot(322)
plt.plot(t,f2)
plt.subplot(323)
plt.plot(t,f1*-f2)
plt.subplot(324)
plt.plot(t,f1*f2)
plt.subplot(325)
def unit(t):
     r=np.where(t>0.0,1.0,0.0)
     return r
t=np.linspace(-1.0,3.0,1000)
plt.ylim(-1.0,3.0)
plt.plot(t,unit(t))
plt.show()
