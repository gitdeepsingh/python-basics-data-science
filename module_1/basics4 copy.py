

#%% 
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
x = np.linspace(-1,20,60)
y = x**3
plt.plot(x,y,'bo')