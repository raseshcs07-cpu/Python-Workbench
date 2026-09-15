# specify data type of variable
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


# type() function.
x = 5
y = "John"             # or 'john'.      String variables can be declared either by using single or double quotes:
print(type(x))
print(type(y))


# Legal variable names: 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange" 

# Python allows you to extract the values into variables from colection like [tuple , list]. This is called unpacking.

fruits = [ "apple" , "banana" , "cheerrryyy" ]
x,y,z=fruits

print(x) 
print(y)
print(z)

# 

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
# You can also use the + operaton [ mathematical operator for no.]


# Create a variable outside of a function, and use it inside the function
x = " awesome"

def myfunc():
    print("Python is" + x )

myfunc()

# 


x = " awesome"

def myfunc():
   x = "fantastic"
   print("python is " + x)
 
myfunc()

print("python is" + x)


# global keyword

def myfunc():
    global y
    y=" rasesh"
    print("my name is" + y)

myfunc()


# 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# type - list , float str , int , tuple , dict , bool 




