# Try Except
"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
# Without the try block, the program will crash and raise an error:


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# You can use the else keyword to define a block of code to be executed if no errors were raised:
#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


# Raise an exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")



try:
  print(x)
except:
  print("An error occurred")
finally:
  print("Execution complete")