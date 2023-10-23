#%% 
from sympy import *

x,y = symbols("x y")

expr = x+x**2

x*expr
#%% 
simplify( (x-y)**2 + (x+y)**2)
#%% 
Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
#%% 
(sin(x)/(1+cos(x))).series(x,0,10)
# %%
