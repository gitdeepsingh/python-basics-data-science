
# %%
# Importing intrinsic libraries:
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('classic')
import seaborn as sns

rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)

# Return the cumulative sum of the elements along a given axis.
y = np.cumsum(rng.randn(500, 6), 0)

plt.plot (x, y)
plt.legend ('ABCDEF', ncol=2, loc='upper left')
plt.show ()

print("y.shape", y.shape)
print("np.shape", np.shape(y))

# %%
# For statistical data visualization, we want to plot histogram and distrit: multivariate_normal
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd. DataFrame (data, columns=['x', 'y'])
for col in 'xy':
    plt. hist (data[col], density=True, alpha=0.7)
#Kernel density estimation using 'kdeplot'


# %%
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('classic')

# A kernel density estimate (KDE) plot is a method for visualizing the
# distribution of observations in a dataset, analogous to a histogram.
# KDE represents the data using a continuous probability density curve in one or more dimensions.

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd. DataFrame (data, columns=['x', 'y'])
for col in 'xy':
    sns.kdeplot(data[col], shade=True)

print("data.shape: ", data.shape)
# %%
# Histograms and KDE combined plot using 'distplot'
# Density Plot with Seaborn defaults
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('classic')
import seaborn as sns


# Density Plot with Seaborn defaults
x,y= np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000).T
sample_cmap = sns.cubehelix_palette(light=1, as_cmap=True)
sns.kdeplot([x, y], cmap=sample_cmap, shade=True)

with sns.axes_style('darkgrid'):
    sns.jointplot("x", "y", data, kind='hex')
# %%
#Pair Plots using the IRIS
import seaborn as sns

iris = sns.load_dataset("iris") # Load the dataset 
iris.head()
# iris.info()
sns.pairplot(iris, hue='species', size=5)
# %%
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('classic')
import seaborn as sns

# exoplanest
planets = sns.load_dataset('planets')
planets.shape
planets.head()
planets.dropna().describe()
planets.groupby('method')['orbital_period' ].median()
#Iteration over groups
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))
# %%
