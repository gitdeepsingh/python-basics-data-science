#%%
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

samples = 3*np.random.randn(1000)+2
a = np.random.randn(300)
b = np.random.randn(300) + 0.1

stats.ttest_ind(a,b)

x = np.hstack(( 2*np.random.randn(1000)+5,  0.6*np.random.randn(1000)-1) )

counts,bins,_ = plt.hist(x)
x_fine=np.linspace(-2,10,100)
pdf = stats.kde.gaussian_kde(x)
print('pdftype=',type(pdf))
plt.plot(x_fine,np.sum(counts)*pdf(x_fine))

# %%
