# def keyword,
# ex.1
def my_function():                    #You can call the same function multiple times
  print("Hello from a function\n")

my_function()
my_function()
my_function()

# Function names follow the same rules as variable names

# why to use it 
# ex.2
def fahrenhait_to_celsius(fahrenhait):
  return (fahrenhait-32)*5/9 

print(fahrenhait_to_celsius(100))
print(fahrenhait_to_celsius(50))
print(fahrenhait_to_celsius(0))


# ex.3
#return statement
def get_help():
 return "\n\n\n\nyes tell i am here"
 
message = get_help()
print(message)

# or 
def get_help():
  return "\n\nyes i am here\n\n"

print(get_help())

# If a function doesn't have a return statement, it returns None by default.


# Arguments

# ex.4
def my_name(fname):              #defing function and fname is parameter
 print(fname + " agarwal\n")     
 #rasesh , tanishk is an argument , which can be called from function value we give 
my_name(" rasesh")
my_name(" tanishkk")

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
# function expects 2 arguments, you must call it with exactly 2 arguments.

# ex.5
def my_function(fname, lname):
  print(fname + " " + lname + "\n")

my_function("rasesh", "agarwal")
my_function("tanishk" , "agarwal" )


# Default Parameter Values

# ex.6
def my_function(name="hemlata"):
  print(name,"agarwal")

my_function("rasesh")
my_function("tanishk")
my_function()


# ex.7
def my_function(state="rajasthan"):
 print("I am from" , state)
my_function("Karnataka")
my_function()
my_function("Uttar pradesh")
my_function("Himachal pradeh\n")


# Keyword Arguments

print(" I have a Dog")
def my_function(animal,name):
  print("\nI have a",animal)
  print("My",animal + "'s name is" , name)

my_function(animal = "dog", name = "stella")
my_function(animal = "cat", name = "Buddy")
my_function(animal ="" , name = "\n")


# positional arguments 

def my_function(animal,name):
  print("\nI Have a",animal)
  print("My",animal + "'s name is" , name)

my_function("dog","stella")
my_function("cat" , "buddy\n")


def my_function(animal,name,age):
  print("I Have a ",age,"year old",animal,", named",name)

my_function("dog",name="stella",age=3,)
my_function("cat",name="buddy\n\n\n",age=2,)


# For loop list ke har element ko ek-ek karke fruit variable me store karta hai.
# First Iteration
# fruit = "apple"
# print(fruit)



# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
# The data type will be preserved inside the function:

def my_function(fruits):
   for fruit in fruits:
    print(fruit)

my_fruits="apple","bannana","cherry"
my_function(my_fruits)

# Memory Flow

# my_fruits
# ↓
# ["apple", "banana", "cherry"]

# ↓ passed as argument

# my_function(my_fruits)

# ↓ received by parameter

# fruits = ["apple", "banana", "cherry"]

# ↓ for loop

# apple
# banana
# cherry


# []list,{}dictionary,()tuple

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Tanishk", "age": 25}                        # dictionary 
my_function(my_person)


# input statement

def my_function(x,y):
    return x + y

x = int(input("write first number:"))
y = int(input("write second number:"))
result = my_function(x,y)
print(result)

# or 

def my_function(x, y):
    return x + y

print(my_function(
    int(input("write first number: ")),
    int(input("write second number: "))
))


# Return Values
# Returning Different Data Types

def my_function(x,y):
    return x*y
result=my_function(5,3)
print(result)

    #  or 

def my_function(x,y):
    return x*y
print(my_function(5,3))



#  Returning Different Data Types

def my_function():
  return ["apple\n","bannana\n","cherry\n"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# input with user 

def my_function():
 A = int(input("Enter the first number: "))
 B = int(input("Enter the second number: "))
 return (A + B)       # returning sum of a,b

# Only use ONE variable here because the function only returns ONE number

Total= my_function()
print("total sum:",Total)  




def my_function():
    A = int(input("Enter the first number: "))
    B = int(input("Enter the second number: "))
    # Return both separate numbers
    return (A, B) 

x, y = my_function()
print("x:", x) # If you typed 10, this prints 10
print("y:", y) # If you typed 20, this prints 20



# Positional-Only Arguments
# To specify positional-only arguments, add , / after the arguments:

def my_function(name, /):
  print("Hello" , name)
my_function("Rasesh")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
# my_function(name = "Emil")

# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*,name):
  print("Hello" , name)
my_function(name="Rasesh")

# Without '*,' you are allowed to use positional arguments even if the function expects keyword arguments:
# my_function("Emil")


# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
# a, b (Positional-only)
# c, d (Keyword-only)



def my_function(name,age,/,*,surname):
  # Using an f-string to format the variables into a clean sentence
  return f"My name is{name} . I am {age} , and My surname is {surname} "
# passing data in function
result = my_function(" Rasesh",19,surname = "Agarwal")
print(result)


# short
 
def my_function(name,age,/,*,surname):
  return (name,age,surname)
print(my_function("Rasesh",19,surname="Agarwal"))




# Arbitrary Arguments [*] - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

def my_function(*kids): 
  print("My name is " + kids[2])

my_function("tanishk","Hemlata","Rasesh")



def my_function(*args):
  print("Type:",type(args))
  print("First arguments:" ,args[0])
  print("Second arguments:" ,args[1])
  print("All arguments:" , args )

my_function("Rasesh","Tanishk","Hemlata")
  


# You can combine regular parameters with *args.
# Regular parameters must come before *args:

def my_function(greetings, *names):         # to put any no. of input
 for name in names:
   print(greetings,name)
my_function("Hello","Rasesh","papa","mumma")
# "Hello" is assigned to greeting, and the rest are collected in names.


#  the function that calculates the sum of any number of values:

def my_function(*numbers):
#"Take all the positional arguments passed into this function and pack them into a single tuple named numbers."
# it can now accept any number of arguments.

  total = 0                                 # initiallization , to keep track of sum
  for num in numbers:                       # iterates numbers tuple one by one 
    total += num                            # adding the no.
  return total                              # once the loop finshes , function returs back to execute

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))





# Max. value 

def my_function(*numbers):

  if len(numbers) == 0:          # for safety , if any number is not in brackett than , system is not crashed , returns a value none 
     
     return None
  
  max_num = numbers[0]           # syntax for maximum number 

  for num in numbers:
    if num > max_num:            # loop will check here one by one 
      max_num = num

  return max_num                 # after checking , function sends retuen value to finally exeute . 

print(my_function(3, 7, 2, 9, 1))
print(my_function(37, 29, 91))



# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

def my_function(**kid):
  print("His last name is" + kid["lname"])
my_function(fname="Rasesh",lname=" agarwal")



def my_function(**myvar):
 print("type:", type(myvar))
 print("Name:", myvar["name"])
 print("Age:", myvar["age"])
 print("City:", myvar["city"])
 print("All data:", myvar)
my_function(name="Rasesh",age=19,city="rajasthan")



# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs:

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():                              # creates details dictionary. Loop through the optional keyword dictionary..items() method lets you grab both the key (e.g., "age")

    my_function("emil123", age = 25, city = "Oslo", hobby = "coding")




# combining *args + **kwargs
# order - regural parameter > *args > **kwargs

def my_function(title,*args,**kwargs):
  print("Title",title)
  print("positional arguments:",args)                                         # Parentheses()
  print("Keywords arguments:",kwargs)                                         # Braces{}

my_function("User info","Rasesh","agarwal",Age=19,city="Rajasthan")           # all arguments , parameter , kwargs



# Unpacking Arguments;(expand)
# lists *

def my_function(a,b,c):
  return a+b+c
numbers = [1,2,3]
result=my_function(*numbers)                                                 #unpacking(*numbers)
print(result)

# dictionary **
 
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)                                                        # Same as: my_function(fname="Emil", lname="Refsnes")





