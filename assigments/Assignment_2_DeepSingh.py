
# ------------ASSIGNMENT 2-----------------
# ANSWER 1
# Using different values of n_refine what changes do we see
'''
  when as we set different values of x_refine, it is observed that
  larger the x_refine value, more precise our interpolations are.
  For Larger values data points are less scattered; i.e. closer to each other and 
  interp1d plots appear comparatively continuous.
'''
# -----------------------------
#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
def create_data(n):
    '''given an integre n, return n data points: x&y as numpy arrays'''
    xmax = 10
    x = np.linspace(0, xmax, n)
    y = -x**2
    y += 1.5*np.random.normal(size=len(x)) #draw random samples from a normal (Gaussian) distribution
    return x,y

n=30
x,y= create_data(100)
plt.plot(x,y, 'b.', label='data points')


n_refine = 3 
xfine = np.linspace(0.1,9.9, n*n_refine)

'''
  # interpolation: determining unknown values that lie in between the known data points
  # interp1d's kind argument specifies piecewise constant function, say p
  # piecewise constant function: where something remains the same for a while, then abruptly changes,
  remains constant again, and so on.
    - constant: Represents data as a sequence of constant values within specific intervals.
    - linear: Represents data as linear segments within specific intervals.
    - quadratic: Represents data as quadratic curves within specific intervals.
    - cubic: Represents data as cubic curves within specific intervals.
'''



# for y0, piecewise constant function: p(0)
y0 = sp.interpolate.interp1d(x,y,kind='nearest')

# for y1, piecewise linear function: p(1)
y1 = sp.interpolate.interp1d(x,y,kind='linear')

# for y2, piecewise quadratic function: p(2)
y2 = sp.interpolate.interp1d(x,y,kind='quadratic')

# for y3, piecewise cubic function: p(3)
y3 = sp.interpolate.interp1d(x,y,kind='cubic')

plt.plot(xfine, y0(xfine), '-r', label="nearest") # TODO: doubt? why y0(xfine); why not y0 only
plt.plot(xfine, y1(xfine), '-y', label="linear")
plt.plot(xfine, y2(xfine), '-g', label="quadratic")
plt.plot(xfine, y3(xfine), '--', label="cubic")

plt.legend()
plt.xlabel('x')


# -----------------------------
#     ANSWER 2
# -----------------------------

#%%
import numpy as np
import matplotlib.pyplot as plt

'''
  numpy.exp: Calculate the exponential of all elements in the input array.
'''

def f1(x, a, b, c):
    ''' fir function: y=f(x,p) where p=(a,b,c)'''
    return a * np.exp(-b*x) + c

def f2(x, a, b, c):
    ''' fir function: y=f(x,p) where p=(a,b,c)'''
    return a * np.sin(b*x) + c

# create fake data
x = np.linspace(0,4,50)
y = f1(x, 2.5, 1.3, 0.5)
z = f2(x, 2.5, 1.3, 0.5)

# add noise
noise_amp = 0.25
yi = y + noise_amp * np.random.normal(size=len(x))
zi = z + noise_amp * np.random.normal(size=len(x))

plt.plot(x, y)
plt.plot(x, yi, '.')
plt.plot(x, z)
plt.plot(x, zi, 'b.')
    

#%%
# ------------3-----------------
#     ANSWER 3
'''
**INSIGHTS**: 
  The plots of f1 and f2 are affected by noise_amp
  Greater the noise_amp, more distorted the function plot and
  the function plots tend to linearity across x-axis
  Noise suppresses the true nature of the function plots.
'''
# -----------------------------

import numpy as np
import matplotlib.pyplot as plt

'''
numpy.exp: Calculate the exponential of all elements in the input array.
'''

def f1(x, a, b, c):
    ''' fir function: y=f(x,p) where p=(a,b,c)'''
    return a * np.exp(-b*x) + c

def f2(x, a, b, c):
    ''' fir function: y=f(x,p) where p=(a,b,c)'''
    return a * np.sin(b*x) + c

# create fake data
x = np.linspace(0,4,50)
y = f1(x, 2.5, 1.3, 0.5)
z = f2(x, 2.5, 1.3, 0.5)

# add noise
noise_amp = 0.25
yi = y + noise_amp * np.random.normal(size=len(x))
zi = z + noise_amp * np.random.normal(size=len(x))

plt.title(f'noise_amp {noise_amp}')
plt.plot(x, y, 'g.', label="f1")
plt.plot(x, yi, 'r', label="f1-normal")
plt.plot(x, z, 'y', label="f2")
plt.plot(x, zi, 'b.', label="f2-normal")
plt.legend()

# %%
# -------------4----------------
#     ANSWER 4
'''
  We often have a dataset comprising of data following a general path,
  but each data has a standard deviation which makes them scattered
  across the line of best fit. We can get a single line using curve-fit() function.

  **INSIGHTS**:
    Without any noise i.e. when noise_amp=0, a,b,c = [2.5 1.3 0.5]
    When noise_amp=1: a,b,c = [2.76897518 1.63078521 0.48984154]
    When noise_amp=10: a,b,c = [ 0.0147829  -1.57621777  0.33097401]

    Larger values of noise_amp => When 50<noise_amp>10: we are getting random abrupt values
    for a,b,c (sometimes very large and sometimes very small or -ve)
    like [-52.83406119 393.11073241   6.07014295] , popt [-32.881333   291.05527898  -0.30460119]

'''
# -----------------------------

import scipy.optimize as spopt
import numpy as np

def f1(x, a, b, c):
    ''' fir function: y=f(x,p) where p=(a,b,c)'''
    return a * np.exp(-b*x) + c

x = np.linspace(0,4,50)
y = f1(x, 2.5, 1.3, 0.5)

noise_amp = 0.25
yi = y + noise_amp * np.random.normal(size=len(x))

popt, pcov = spopt.curve_fit(f1, x, yi)
a,b,c = popt
print("Optimal parameters are a=%g, b=%g and c=%g" % (a,b,c))



# %%
