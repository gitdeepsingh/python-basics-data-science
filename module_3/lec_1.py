#%%
import pandas as pd;
import seaborn as sns
import scipy as sc
import scipy.interpolate as intplt
import scipy.constants as sc_c
import numpy as np
import matplotlib.pyplot as plt

# %%
import scipy.constants as sc_c

print ("physical_constants: ", sc_c.physical_constants['electron volt-joule relationship' ])

# %%
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline
import scipy.integrate as sc_integ

# Define a function.
def IntFunc(x):
    return 1./x**2 + 0.6*np.sin(x) - np.sqrt(x)

# Plot the function.
x = np.linspace(1.0, 15.0,256)
y = IntFunc(x)
plt.plot(x, y, 'k', lw=2)
plt.plot([4.0,4.0],[-4.0,IntFunc(4.0)], 'b--',lw=2)
plt.plot([14.0,14.0],[-4.0,IntFunc(14.0)], 'b--',lw=2)
in1 = np.abs(x-4.0).argmin()
in2 = np.abs(x-14.0).argmin()
plt.fill_between(x[in1:in2], -4.0, IntFunc(x[in1:in2]),color='yellow',alpha=0.4)
plt.xlabel(r'X axis')
plt.ylabel(r'F(x)')
plt.minorticks_on()


# # Integrate.
ans_q1 = sc_integ.quadrature(IntFunc, 4.0, 14.0, rtol=1.0e-8) 
ans_q2 = sc_integ.quad(IntFunc, 4.0, 14.0)
print(ans_q1)
print(ans_q2)


#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc_integ

#TODO: what is difference btw quadrature and quad

'''
   quad          -- General purpose integration.
   dblquad       -- General purpose double integration.
   tplquad       -- General purpose triple integration.
   fixed_quad    -- Integrate func(x) using Gaussian quadrature of order n.
   quadrature    -- Integrate with given tolerance using Gaussian quadrature.
   romberg       -- Integrate func using Romberg integration.
'''

# TODO: check above on Gaussian function, check previous assignments for GF
def GaussianFun(x):
    return np.exp(- x**2)

x = np.linspace(1.0, 15.0,256)
y = GaussianFun(x)
plt.plot(x, y, 'k', lw=2)
plt.plot([4.0,4.0],[-4.0,GaussianFun(4.0)], 'b--',lw=2)
plt.plot([14.0,14.0],[-4.0,GaussianFun(14.0)], 'b--',lw=2)
in1 = np.abs(x-4.0).argmin()
in2 = np.abs(x-14.0).argmin()
plt.fill_between(x[in1:in2], -4.0, GaussianFun(x[in1:in2]),color='yellow',alpha=0.4)
plt.xlabel(r'X axis')
plt.ylabel(r'F(x)')
plt.minorticks_on()

ans_q3 = sc_integ.quadrature(GaussianFun, 4.0, 14.0, rtol=1.0e-8) 
ans_q4 = sc_integ.quad(GaussianFun, 4.0, 14.0)
print("ans_q3: ", ans_q3)
print("ans_q4: ", ans_q4)

# %%
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline
import scipy.integrate as sc_integ

x = np.linspace(-2.0*np.pi, 2.0*np.pi,128)
y = 2.0*np.exp(-x*x/5.0) + 0.2*np.random.rand(128)
plt.scatter(x, y)

print("Trapezoidal rule : %12.6e"%sc_integ.trapz(y,x=x)) # TODO:
print("simpson's rule : %12.6e"%sc_integ.simps(y,x=x)) # TODO:


# %%
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline
import scipy.integrate as sc_integ

x = np.linspace(-2.0*np.pi, 2.0*np.pi,512)
y = 2.0*np.exp(-x*x/5.0) + 0.2*np.random.rand(512)
plt.scatter(x, y)

'''
Methods for Integrating Functions given fixed samples.

   trapezoid            -- Use trapezoidal rule to compute integral.
   cumulative_trapezoid -- Use trapezoidal rule to cumulatively compute integral.
   simpson              -- Use Simpson's rule to compute integral from samples.
   romb                 -- Use Romberg Integration to compute integral from
                        -- (2**k + 1) evenly-spaced samples.
'''

print("Trapezoidal rule : %12.6e"%sc_integ.trapz(y,x=x)) 
print("simpson's rule : %12.6e"%sc_integ.simps(y,x=x)) 

# TODO: why changing to 512, graph is different, how, what, why. Also try 1024 (max possible)

'''
it depicts no. of point to represent the graph, try 4
'''

# %%
