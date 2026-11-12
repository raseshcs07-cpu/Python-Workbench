# open file:
f = open("demofile.txt", "r")
print(f.read())


"""
"r" - Read 
"a" - Append 
"w" - write
"x" - Create 
"t" - Text 
"b" - Binary 
"""


f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())


with open("demofile.txt") as f:
  print(f.read())


f = open("demofile.txt")
print(f.readline())
f.close()


with open("demofile.txt") as f:
  print(f.read(5))
  print(f.readline())
  print(f.readline())


with open("demofile.txt") as f:
  for x in f:
    print(x)


# append
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())


# write
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


# create
f = open("myfile.txt", "x")


# delete
import os 
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else :
  print("file does not exist")


import os
os.rmdir("myfolder")