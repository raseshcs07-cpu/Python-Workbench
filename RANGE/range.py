# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# range(start, stop, step)
# If the range function is called with only one argument, the argument represents the stop value.
# The start argument is optional, and if not provided, it defaults to 0.
# range(10) returns a sequence of each number from 0 to 9. 
# (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).

x= range(10)
print("\n",x)
print("\n",list(x))

x = range(3, 10)
print("\n",x)
print("\n",list(x))

x = range(3, 10, 2)
print("\n",x)
print(list(x),"\n")

for x in range(10):
  print(x) 

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

# Slicing Ranges
r = range(10)
print(r[2])
print(list(r[:3]))

r = range(10)
print(r[2])
print(r[:3])

# Ranges support membership testing with the in operator.
r = range(0, 10, 2)
print(list(r))
print(6 in r)
print(7 in r)

r = range(0, 10, 2)
print(len(r))

# Print 0 through 5
for x in range(6):
  print(x)

# Print 2 through 5
for x in range(2, 6):
  print(x)