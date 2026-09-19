# While Loops
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

# break statement 
i = 1
while i<6:
  print("\n",i)
  if i == 2:
    break 
  i+=1

# continue
i = 0
while i < 6:
  i += 1
  if i == 3:               # Note that number 3 is missing in the result
    continue
  print("\n",i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("\ni is no longer less than 6")


# Create the i variable
i = 0

# While loop: print 1-5, skip 3 with continue
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)