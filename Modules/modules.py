# Modules
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py:

def greeting(name):
  print("Hello, " + name)

import modules
modules.greeting("Jonathan")



person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import modules
a = modules.person1["age"]
print(a)

# You can name the module file whatever you like, but it must have the file extension .py
# You can create an alias when you import a module, by using the as keyword:
import modules as mx
a = mx.person1["country"]
print(a)

# Built-in Modules
import platform
x = platform.system()
print(x)

# Using the dir() Function
# Note: The dir() function can be used on all modules, also the ones you create yourself.
import platform
x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from modules import person1
print(person1["age"])


# Import the platform module
import platform
# Print the system platform
print(platform.system())