
# -----------------------------
#     ANSWER 1
# -----------------------------
# capture time of execution in block of code.
# check inbuilt factorials of numpy and scipy and compare time of execution for both;

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


# -----------------------------
#     ANSWER 2
# -----------------------------
# Change this x and y axis to only give 4 values along each x and y.
# Change the tick marks, increment as y -> (-0.5,0,0.5,1) | x -> (0,2,4,6)

import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0.,2.*np.pi,100)
plt.plot(a, np.sin(a), 'r--')
plt.plot(a, np.sin(8*a), 'g--')

plt.xticks(np.arange(0, 8, step=2)) # set xticks
plt.yticks(np.arange(-0.5, 1.5, step=0.5)) # set yticks

plt.xlabel('a')
plt.ylabel('sin(a)')
plt.title('My Plot')