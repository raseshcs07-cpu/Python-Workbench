# for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["\napple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["\napple", "banana", "cherry"]
[print(x) for x in thislist]

# While Loop
thislist = ["\napple", "banana", "cherry\n"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# x = "ilove you"
# i = 0
# while i  < 1000:
#   print(x)
#   i = i + 1


# List Comprehension
fruits = ["apple","banana","cherry","kiwi",",mango"]
newlist = []
for x in fruits:
  if 'a' in x:
    newlist.append(x)
print(newlist)

fruits = ["apple","banana","cherry","kiwi",",mango"]
newlist=[x for x in fruits if 'a' in x]                              #The Syntax
                                                    # newlist = [expression for item in iterable if condition == True]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print("\n\n",newlist)

list=[x for x in range(100)]
print("\n\n",list)

newlist = [x for x in range(10) if x < 5]
print("\n",newlist)

newlist=[x.upper() for x in fruits]
print("\n",newlist)

newlist=['hello' for x in fruits]
print("\n",newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print("\n",newlist)
# "Return the item if it is not banana, if it is banana return orange".


# Sort Lists
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# reverse = True: Sort Descending
thislist=[1,2,3,4,5,6,7,8,]
thislist.sort(reverse=True)
print(thislist)

# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("\n",thislist)
# key=myfunc does not change the actual numbers.

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("\n",thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print("\n",thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("\n",thislist) 


# Copy Lists
thislist=["apple","banna","cherry","mango"]
mylist=thislist.copy()
print("\n",mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

thislist = ["apple","banana","cherry"]
mylist = thislist[ : ]
print("\n",mylist)


# Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print("\n",list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print("\n",list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("\n",list1)

"""
append()	Adds an element at the end of the list
clear()	  Removes all the elements from the list
copy()	  Returns a copy of the list
count()	  Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	  Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	  Sorts the list
"""

# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1] = "yellow"
# Add "purple" to the end
colors.append("purple")
# Remove "red"
colors.remove("red")
# Print the list
print(colors)
