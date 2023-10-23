#############################################
# TODO: 1: 
# how to capture time of execution in block of code? 
# Use below for larger numbers;
# check inbuilt factorials of numpy and scipy and compare time of execution for both;

#%%
import timeit
npfact_code = '''
import numpy as np
def np_fact(num):
    return np.math.factorial(num)
'''
scfact_code = '''
from scipy.special import factorial
def sp_fact(num):
    return factorial(num)
'''

code_setup = '''
def fact(x):
    if (x == 0):
        return 1
    if (x < 0):
        return "Negative Factorial not defined"
    arg = x
    while(x>1):
        arg = arg*(x-1)
        x = x-1
    return arg
'''

seconds_fact = timeit.timeit('fact(500)',setup = code_setup, number=1000)
seconds_npfact = timeit.timeit('np_fact(500)',setup = npfact_code, number=1000)
seconds_spfact = timeit.timeit('sp_fact(500)',setup = scfact_code, number=1000)
print("The time of execution of custom factorial :", seconds_fact)
print("The time of execution of numpy factorial :", seconds_npfact)
print("The time of execution of scipy factorial :", seconds_spfact)

if seconds_fact <= seconds_npfact and seconds_fact <= seconds_spfact:
  fastest='custom'
elif seconds_npfact <= seconds_fact and seconds_npfact <= seconds_spfact:
  fastest='numpy'
else:
  fastest='scipy'

print('----------------------------------------------------------------')
print('fastest factorial: ', fastest.upper())

#%%
############################################

# list
cols=["Red","Green", "White"]
cols.append("Yellow")
cols.extend("Black") # iterates over Black
cols.insert(2,"Purple")
print('3:=', cols)

###############################################

# array
arr = [1,2,3,100]
import numpy as np
arr=np.asarray(arr) # converts to list
print('4:=', arr.shape)

##############################################

# plotting
cc=np.arange(0,10); print('5:=', cc)
dd=np.linspace(0,10,10,endpoint=False);print('6:=', dd)

#%%
import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0.,2.*np.pi,100)
plt.plot(a, np.sin(a), 'r--')
plt.plot(a, np.sin(8*a), 'g--')

# TODO: 2:
# Change this x and y axis to only give 4 values along each x and y.
# Change the tick marks, increment as y -> (-0.5,0,0.5,1) | x -> (0,2,4,6)
plt.xticks(np.arange(0, 8, step=2)) 
plt.yticks(np.arange(-0.5, 1.5, step=0.5)) 

plt.xlabel('a')
plt.ylabel('sin(a)')
plt.title('My Plot')


# %%
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-np.pi, np.pi,256, endpoint=True)
C, S=np.cos(x), np.sin(x)
plt.plot(x,C, '.', color='blue')
plt.plot(x,S, '--', color='red')
# %%
#interoplation
import scipy as sc
import scipy.interpolate as intplt
import numpy as np
import matplotlib.pyplot as plt

def create_data(n):
    """given an integer,return n datapoints, x and y values as numpy.array"""
    xmax=10
    x=np.linspace(0,xmax,n)
    y= - x**2
    y += 1.5 * np.random.normal(size=len(x))
    y = -x**2 + 1.5 *np.random.normal(size=len(x))
    return x,y

x,y = create_data(30)
print('7:=',x)

plt.plot(x,y, '.b', label="data points")
plt.legend()
##############################################
