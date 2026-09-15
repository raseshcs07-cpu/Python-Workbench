#  decorators : to add extra behaviour to a function , withot changing the function's cod . 
#  it takes another function as input  , return a new function  . 



# ex. 1
# A basic decorator that uppercases the return value of the decorated function. 

def changecase(func):     
    def myinner():
        return func().upper()
    return myinner()
 
@changecase                                   # decorator

def myfunction():                             # decorated  
    return "Hello Rasesh"
print(myfunction)

# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.


 
#  Multiple decorators :

# Ex. 2 
# Using the @changecase decorator on two functions:

def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase

def myfunction():
    return "Hello Rasesh\n"
@changecase

def myouter():
    return "I am Delelu"

print (myfunction()) 
print (myouter())



# Ex. 3
# Decorated can also use functions  with Args. 

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))



# *args and **kwargs
# ex. 4
# Secure the function with *args and **kwargs arguments:

def changecase(func):
 def myinner(*args,**kwargs):
  return func(*args,**kwargs).upper()
 return myinner

@changecase

def myfunction(nam):
 return "Hello " + nam
print (myfunction("Rasesh"))



# decorator + args. 
# Ex. 5
# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n==1:
        a = func().lower()
      else :
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(11)
def myfunction():
  return "hello Rasesh "
  
print(myfunction())



# Multiple Decorators
# This is done by placing the decorator calls on top of each other.

# Ex. 6
# One decorator for upper case, and one for adding a greeting:


def changecase(func):
 def myinner():
  return func().upper()
 return myinner
 
def addgreeting(func):
 def myinner():
  return "Hello " + func() + " have a good day "
 return myinner
 
@changecase
@addgreeting

def myfunction():
 return "Rasesh"
print(myfunction())


# Preserving Function Metadata
# Ex .7
#  Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Who are you ?"
print(myfunction.__name__)

# Ex. 8
# But, when a function is decorated, the metadata of the original function is lost.
# Try returning the name from a decorated function and you will not get the same result:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


# ex.9
# Import [# functools.wraps] to preserve the original function name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper
  return myinner 
@changecase
def myfunction():
  return " hello RAsesh "
print(myfunction.__name__)

# Ex.10
def upper(f):
  def w():
    return f().upper()
  return w

def exclaim(f):
  def w():
    return f() + "!"
  return w

@upper
@exclaim
def say():
  return "hi"

print(say())
