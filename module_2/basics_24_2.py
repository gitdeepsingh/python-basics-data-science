#%%
import pandas as pd
import seaborn as sns
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()

#Using seaborn package explore the dependency of arr_delay on dep_delay (Il

'''
    The plot of regression in a seaborn is primarily intended to add
    a visual guide for emphasizing the patterns from the dataset during
    data analysis. As the name suggests regression plot creates the line
    of regression between two different parameters, and it will help us
    visualize the linear relationships. Seaborn is providing built-in datasets.
    It is not only the visualization library.
'''
# Plot data and a linear regression model fit.
sns.regplot(x='arr_delay', y='dep_delay', data=flights2)

# %%
import pandas as pd
import seaborn as sns
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()

sns.pairplot(flights2) # how correlated the fields are to each other
# %%
import pandas as pd;
from pandas import Series, DataFrame
#Read csv file :
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
sns.pairplot(df)

# %%
