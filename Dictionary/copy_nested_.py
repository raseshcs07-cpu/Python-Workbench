# Copy :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.copy()
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict(thisdict)
print(x)


# Nested :
myfamily = {
    "Child1": {
        "name": "emil",
        "year":2026
    },
    "Child2": {
        "name" : "Rasesh",
        "year" : 2027
    },
    "Child3": {
        "name": " tanishk",
        "year": 2028
    }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily= {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print(myfamily["child1"]["name"])

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
     print(y + ":", obj[y])


"""
clear()	      Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys      ()	Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
"""


a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name'])

# Create the dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 2024}
# Print the model
print(car["model"])
# Add a color key
car["color"] = "red"
# Remove the brand key
car.pop("brand")
# Print the dictionary
print(car)