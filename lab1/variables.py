#ex1
x = 5
y = "John"
print(x)
print(y)

#ex2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#ex3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#ex4
x = 5
y = "John"
print(type(x))
print(type(y))

#ex5
x = "John"
# is the same as
x = 'John'

#ex6
a = 4
A = "Sally"
#A will not overwrite a

#ex7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#ex8
myVariableName = "John" #camelCase
MyVariableName = "John" #PascalCase
my_variable_name = "John" #snake_case

#ex9
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ex10
x = y = z = "Orange"
print(x)
print(y)
print(z)

#ex11
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#ex12
x = "Python is awesome"
print(x)

#ex13
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#ex14
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#ex15
x = 5
y = 10
print(x + y)

#ex16
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#ex17
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#ex18
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#ex19
