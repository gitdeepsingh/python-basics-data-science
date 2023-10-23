#%% 
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from scipy import optimize
x = np.linspace(-1,2,5)
y = x**3

f = interp.interp1d(x,y,kind="linear")
x_fine = np.linspace(-1,2,100)
plt.plot(x_fine,f(x_fine))

# %%
a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape
