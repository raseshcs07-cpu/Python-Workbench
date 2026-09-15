
# A variable is only available from inside the region it is created. This is called scope.
# local scope - a variable created inside  a function 

def myfunc():
  x = 300
  print(x)

myfunc()



# function in function 

def myfunc():
  x=300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global Scope - a variable created in python code's main body , they are available inside scope.global,local.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)



# Naming Variables - global scope + local scope


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)



# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.


def myfunc():
  global x
  x = 300

myfunc()

print(x)


# Nonlocal Keyword - used to work with variables inside nested functions.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


# legb rule - for looking up variable names 
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace



x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)






  