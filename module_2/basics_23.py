#%%

import pandas as pd;
from pandas import Series, DataFrame
print(pd.__version__)

'''
    A Data frame is a two-dimensional data structure, i.e., data is aligned
    in a tabular fashion in rows and columns. Pandas DataFrame consists of
    three principal components, the data, rows, and columns.
'''

obj= Series([2,-4,8,0]) #pandas label data in format
print('----obj----') 
print(obj) 
print(obj.index)
print('------------') 

sdata={ 'Radio': 'VLA', 'Xray': [ 'Chandra', 'XMM Newton '], 'Optical': 'Hubble'}
print('sdata----')
print(sdata.values(), '------', sdata.keys())

print(sdata["Radio"])

sdata.update({'Radio': ['VLA', 'SMA', 'PdBI']})
print(sdata.values())

obj2=Series(sdata)
print('---obj2---')
print(obj2)

# %%
import pandas as pd;
from pandas import Series, DataFrame

Indian_City={'state': ['MP', 'MP', 'Delhi', 'MH', 'MH', 'UP'],
'year': [2010,2015,2010,2010,2015,2010],
'pop': [10,15,20,20,40,5017]}

frame=DataFrame(Indian_City)
print('-----frame-----')
print(frame)

#Create as Series from a dictionary
data = {'a': 10, 'b':6, 'c':2,'d':7}
s3=Series(data)
print('s3----')
print(s3)

s4 = Series(s3, index = ['a', 'b', 'c', 'e', 'd'])
print('----s4---')
print(s4)

# %%
import pandas as pd;
from pandas import Series, DataFrame

s1 = Series( [0,2, 9, 6, -4, 8, -10] )

print('----s1-----')
print(s1[(s1>0)])
print('----')
print(s1[(s1>0) & (s1<s1.mean())])
print('---------')
print(s1[:2])
print('---------')
print(s1.iat[-1])
print('---------')
print(s1.mean())
print('---------')
print(s1.median())
print('---------')

# %%
import pandas as pd;
from pandas import Series, DataFrame

d1 = pd. DataFrame ( { 'Name': pd.Series ( ['Chris', 'James', 'Tom' ]),
'Age': pd.Series ( [23,29,25]) } )

print('-----d1-----')
print(d1)

# %%
import pandas as pd;
from pandas import Series, DataFrame
#Read csv file :
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
print('df------')
print(df)
print('---------')
print(df.info())
# print(df.tail(10))
print('---------')
print(type(df))
print('---------')
print(df['salary'].dtype)
print('---------')
print(df.dtypes)
print('---------')
print(df.columns)
print('---------')
print(df.size)
print('---------')
print(df.shape)
print('---------')
print(df.describe()) # provides numeric datas, avoids non-numeric

print('---------')
print('----mean salary-----')
print(df.salary.mean())




# %%
import pandas as pd;
from pandas import Series, DataFrame
#Read csv file :
df = pd.read_csv("http://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")
print('df------')
df_rank=df.groupby('rank').rank()
print('df_rank---')
print(df_rank)

# Group using 2 variables - sex and rank:
df.groupby( [ 'rank', 'sex'], sort=True) [ ['salary' ]].mean () # TODO: groupby is important

#Selected data for female professors :
df_w = df[df.sex =='Female']
df_w.count( )

df.rename (columns = {'rank': 'Designation '}, inplace = True)
print(df.info)
# %%
