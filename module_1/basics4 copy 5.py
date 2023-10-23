#%% 
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from scipy import optimize
import scipy.integrate as integ

def f(y,t):
    return (y[1], -y[1]-9*y[0])

t = np.linspace(0,10,100)
Y = integ.odeint(f,[1,1],t)

plt.plot(t,Y[:,1])


# %%
