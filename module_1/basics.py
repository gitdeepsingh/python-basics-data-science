print('Hello World')

x='Deep'
x=2
print(x) # test comment

print('a' == 'A')
print('Multiplication:', x*30)
print("floor value", 100//8)
print("int + string", 5+True)

# pyhon compares value, not type for numbers
print('int and float comparison for same value; ', 5.0 == 5)

name='Devyani'
print(f"{name} is here")

'''
comments
'''

for i in range(5):
    print('i=',i,'|', end='') # end avoids moving to new line

for i in range(10,2,-2): # (start, end, difference)
    print('i=',i)


try:
    100/0
    print('all good')
except ZeroDivisionError:
    print('ZeroDivisionError')


print('============')
ans=0
# print all powers of 2 less than 10000
for i in range(10000):
    if 2**i < 10000:
        ans=2**i
    else:
        break
print('answe=', ans)
print('============')

'''
i = 1
while (2^i) < 10000:
     print(2^i)
     i +=1
'''

a=1;b=2;print('1:=', a,b)
a,b,c=100,3*a,4+a-b;print('2:=', a,b,c)


n=0
i=0
while i<=10000:
    n+=1
    i=2**n
    if i<=10000:
        print(n,":",i)

# almost in python is object, can be passed to a fxn

def greet(name="XXXX"):
    return print(f'''Hello {name}''')


def greet2(*names): # names tuple
    for name in names:
        print(f"Hello {name}", end=' | ')

greet2('deep', 'devu', 'tanmay')

cube= lambda x: x*x*x
print('cube lambda', cube(3))

def nothing():
    """"This function just nothing"""
    pass

#help(nothing)


#------------------------------------------------------#
# LIST
listA= [1, "days", "some", 2.3]
print(listA[0])
print(listA[-1]) # last element

print("listA elements: ")
for ele in listA:
    print(ele)

print(listA*2) # duplicates twice

# operations on list: append, insert, pop, extend, filter, map

a=[]
print(a)
for i in range(10):
    a.append(i*2)
    print(a)
    
# a.pop?

b=a # shallow copy
print('b: ',b)
b.pop()
print('a:', a) # a changes, so = copy changes original also


c=[1,2,3]
d=c.copy() # deep copy
print('d:', d)
d.pop()
print('d: on pop', d)
print('c: on pop on d', c) # remains same as original


print('addresses to learn copy : ', id(a), id(b), id(c), id(d))

for idx, ele in enumerate(a):
    print(idx, ':', ele)

# filterres= list(lambda x: x%2==0)
# print('filtered a: ', list(filterres))


