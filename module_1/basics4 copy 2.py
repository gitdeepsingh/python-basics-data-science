
#%% 
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)

plt.imshow(X**2+Y**2)# %%


# %%
