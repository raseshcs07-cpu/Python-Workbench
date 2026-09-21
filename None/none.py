# None
# None is a special constant in Python that represents the absence of a value.
x = None
print(x)

x = None
print(type(x))

# operator is or is not
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

print(bool(None))

def myfunc():
 x = 5
x = myfunc()
print(x)


# Assign None to x
x = None
# Check if x is None
if x is None:
  print("x is None")