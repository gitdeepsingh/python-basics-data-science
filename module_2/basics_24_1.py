#%%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights.head(20)

print(flights.info())
print('----------------------------')
print('missing data:')
flights[flights.isnull().any (axis=1)].head() # find nulls; missing values

flights2 = flights.dropna() # drop all Nulls and store updated in flights
print('----------nulls dropped at 14------------------')
flights2[flights2.isnull ().any(axis=1)].head() # check by commenting 14,15,16 lines
flights2.info()

# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights[flights.isnull().any (axis=1)].head() 
# Fill hissing values with zeros :
nomiss=flights['dep_delay' ].fillna(0)
nomiss.isnull().any()
flights.info()


# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna() 

print(flights.describe())
print('-----------flights2 has lesser count as we dropped NANs-----------------')
print(flights2.describe())

# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()

# Summary statistic as per group :
flights2.groupby('carrier')['dep_delay'].mean ()
# flights2.groupby('carrier')['arr_delay'].mean ()
# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()

# Use agg() methods for aggregation :
flights2[[ 'dep_delay','arr_delay']].agg(['min', 'mean', 'max'])
# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()
# Compute different statistics for different columns :
flights2.agg({'arr_delay': [min, 'mean', max],'carrier': ['nunique']})

# %%
import pandas as pd;
from pandas import Series, DataFrame

# Read a dataset with missing values :
flights = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")
flights2 = flights.dropna()
# Convinient describe ( ) function :
flights2.arr_delay.describe() # quartile wise wise


# %%
