#%%
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

samples = 3*np.random.randn(1000)+2
plt.hist(samples)

stats.norm.fit(samples)

# %%
