#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

# read csv file
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

plt.hist(df['salary'], bins=10, density=True); # ; avoids printing dataset values

# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

sns.distplot(df['salary']); 

'''
    Figure-level interface for drawing distribution plots 
    onto a FacetGrid.
    This function provides access to several approaches for
    visualizing the univariate or bivariate distribution of data,
    including subsets of data defined by semantic mapping and
    faceting across multiple subplots.
'''
 #TODO: what is distplot plotting

#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

sns.histplot(df['salary']); 

#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

# Matplotlib function to display a barplot
df.groupby(['service'])['salary'].count().plot(kind="bar"); 
df.head(10)

#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

df.groupby(['rank'])['salary'].count().plot(kind="bar"); 


#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
df.rename(columns = {'rank': 'designation '}, inplace = True)

sns.set_style('whitegrid')
ax = sns.barplot(x='designation',y ='salary', data=df, estimator=np.mean,ci=None)

#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

sns.set_style('whitegrid')
# Split into two groups :
ax = sns.barplot(x='designation',y ='salary', hue='sex', data=df)#, estimator=len)



#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

sns.pairplot(df)
# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

#Scatterplot using seaborn :
sns.jointplot(x='service', y='salary', data=df)

# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

#Linear regression plot for two numeric variables using regplot :
sns.regplot(x='service', y='salary', data=df)

# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

sns.boxplot(x='rank', y='salary', data=df) # TODO: candle plot


# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
sns.swarmplot(x='rank', y='salary', data=df)

# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

# %%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")