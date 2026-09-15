#  Loop Lists

#  for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["\napple","banana","cherry\n"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#  While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

x = "ilove you"
i=0
while i<1000:
  print(x)
i+1


# List Comprehension
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name
fruits = ["apple", "banana", "cherry ","kiwi" , "mango"]
newlist = []

for x in fruits:
  if 'a' in x:
