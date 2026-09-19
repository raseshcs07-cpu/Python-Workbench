#  For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x,"\n")

for x in "banana":
  print(x,"\n")


# break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x,"\n")
  if x == "banana":
    break
print("banana is in th list ","\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x,"\n")


# continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x,"\n")


# range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and ends at a specified number.

for x in range(6):
  print(x,"\n") 

for x in range(2, 6):
  print(x,"\n")

for x in range(2,100,9):
  print(x,"\n")

for x in range(9):
  print(x)
else:
  print("NOW , finished!")
print("\n")

for x in range(9):
  if x==3:
    break
  print(x)
else:
  print("Finally finished!")                            #If the loop breaks, the else block is not executed.
print("\n")


# Nested
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["Lambu","bona"]
Noun=["Rasesh", "TAnishk"]
for x in adj:
  for y in Noun:
   print(x,y)

for x in [0, 1, 2]:
  pass