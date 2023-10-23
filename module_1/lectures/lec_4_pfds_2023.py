# -*- coding: utf-8 -*-
"""Lec_4_PFDS_2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gJlE6zGjK2N84SecfF-P91JTQmtDtfBp

# Keyword arguments in Python Functions
"""

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Alpana")
greet("Ravi", "How do you do?")

# 2 keyword arguments
greet(name = "Ravi",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Ravi")

#1 positional, 1 keyword argument
greet("Ravi", msg = "How do you do?")

# Wrong use
greet(name="Ravi","How do you do?")

def h(a, b, x=3,y=2):
    return a * x + b*y

def g(a, x, b=0):
    return a * x + b

h(1,1,y=1) #equivalent to h(1,1,3,1)

g(2, 5, 1)

g(2, 5)

"""# Python Arbitrary Arguments

Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.
"""

def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Amit", "Sneha", "Rakesh", "Megha")

greet("Amit", "Sneha", "Rakesh", "Megha", "abc")

"""# Python Lambda
An alternative way to define short functions
"""

cube = lambda x: x*x*x
print(cube(4))

cube(5)

"""# Docstring
It is important that others are able to
understand what your code does.
---

"""

def nothing():
  """ This function doesn’t do anything. """
  pass

help(nothing)

"""# Exercise 1

(10 minutes)

1. Write a function that takes two inputs, $a$ and $b$ and returns the value of $a+2b$
1. Write a function takes a number $n$ as input, and prints all [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) less than $n$
"""

#YOUR CODE HERE

"""# Lists

A list in Python is an ordered (and indexed) collection of objects
"""

a = ['x', 1, 3.5]
print(a)
a[0]

"""You can iterate over lists in a very natural way"""

for elt in ["step1", "step2"]:
    print(elt)

"""Python indexing starts at 0."""

a[0] = "overwritten"
a

#can even put functions and other lists inside of lists!
def f(x):
    return x

b = [f, [1,2,2.1]]
print(b)

"""You can append to lists using `.append()`, and do other operations, such as `pop()`, `insert()`, etc."""

a = []
print(a)
for i in range(10):
    a.append(i**2)
    print(a)

while len(a) > 0:
    elt = a.pop()
    print(f"Removed {elt}, a is now {a}")

a = [1,2,3]
a.insert(1,'new value')
print(a)

a.remove?

a = [1,2,3]
b = ["x", "y"]
a.extend(b)
print(a)

a+b

print(f"a + [1,2]: {a + [1,2]}")

"""Python terminology:
* a list is a "class"
* the variable `a` is an object, or instance of the class
* `append()` is a method

Lists in python are only implicitly collections of the objects that constitute them. Setting one array equal to another can lead to unexpected results:
"""

b = a.copy() # deep
b = a #shallow
print(f"original a:, {a}")
print(f"original b:, {b}")
b[0] = "edited"
print("after edit...")
print(f"a:, {a}")
print(f"b:, {b}")

a.copy?

"""A list only stores some pointers to locations in your computer's memory: when we wrote `b = a` Python created a new list `b` which shares its entries with `a`.

The function `.copy()` will create a completely distinct copy with new objects.

## List Comprehensions

Python's list comprehensions let you create lists in a way that is reminiscent of set notation

$$ S = \{ \sqrt{x} ~\mid~ 0 \le x \le 20, x\mod 3 = 0\}$$
"""

import math
S = [math.sqrt(x) for x in range(21) if x % 3 == 0]
S

S= []
for x in range(21):
    if x % 3 == 0:
        S += [math.sqrt(x)]
S

S = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            if (i + j + k)%2 == 0:
                S += [(i,j,k)]

S

# you aren't restricted to a single for loop
S = [(i,j,k) for i in range(2) for j in range(2) for k in range(2) if (i + j + k)%2 == 0]
S

"""Syntax is generally
```python3
S = [<elt> <for statement> <conditional>]
```

# Other Collections

We've seen the `list` class, which is ordered, indexed, and mutable.  There are other Python collections that you may find useful:
* `tuple` which is ordered, indexed, and immutable
* `set` which is unordered, unindexed, mutable, and doesn't allow for duplicate elements
* `dict` (dictionary), which is unordered, indexed, and mutable, with no duplicate keys.
"""

a_tuple = (1, 2, 4)
a_tuple[0] = 3

a_set = {5, 3, 2, 5}
for i in a_set:
    print(i)

a_set.add(6)
a_set.remove(6)
a_set

a_dict = {}
a_dict[5] = 12
a_dict["key_2"] = 27
a_dict["key_3"] = [13, "value"]
a_dict[5] = "new value"
a_dict["key_2"] = 28
a_dict

a_dict_copy = {5: 'new value', 'key_2': 28, 'key_3': [13, 'value']}

"""# Exercise 2

**Lists**
1. Create a list `['a', 'b', 'c']`
2. use the `insert()` method to put the element `'d'` at index 1
3. use the `remove()` method to delete the element `'b'` in the list

**List comprehensions**
1. What does the following list contain?
```python
X = [i for i in range(100)]
```
2. Interpret the following set as a list comprehension:
$S_1 = \{x\in X \mid x\mod 5 = 2\}$
3. Intepret the following set as a list comprehension: $S_2 = \{x \in S_1 \mid x \text{ is even}\}$
4. generate the set of all tuples $(x,y)$ where $x\in S_1$, $y\in S_2$.

**Other Collections**
1. Try creating another type of collection
2. try iterating over it.
"""



"""# Classes

Classes let you abstract away details while programming.
"""

class Animal:
    def say_hi(self):
        print("Hello!")

x = Animal()
x.say_hi()

"""## Example: Rational Numbers

Here we'l make a class that holds rational numbers (fractions).  That is, numbers of the form
$$r = \frac{p}{q}$$
where $p$ and $q$ are integers
"""

class Rational:
    def __init__(self, p, q=1):

        if q == 0:
            raise ValueError('Denominator must not be zero')
        if not isinstance(p, int):
            raise ValueError('Numerator must be an integer')
        if not isinstance(q, int):
            raise ValueError('Denominator must be an integer')

        g = math.gcd(p, q)

        self.p = p // g # integer division
        self.q = q // g

    # method to convert rational to float
    def __float__(self):
        return self.p / self.q

    # method to convert rational to string for printing
    def __str__(self):
        return f'{self.p}/{self.q}'

    def __repr__(self):
        return f'Rational({self.p}, {self.q})'

a = Rational(6, 4)
b = Rational(3, 2)

print(type(a))
print(f"a = {a}")
print(f"b = {b}")
print([a,b])
print(f"float(a) = {float(a)}")

a + b

"""You can do cool things like overload math operators.  This lets you write code that looks like you would write math.  Recall

$$ \frac{p_1}{q_1} + \frac{p_2}{q_2} = \frac{p_1 q_2 + p_2 q_1}{q_1 q_2}$$

We'll see this next time!
"""