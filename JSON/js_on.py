# JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# JSON in Python

# If you have a JSON string, you can parse it by using the json.loads() method.
# JSON to Python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'         # some JSON:
y = json.loads(x)                                            # parse x:
print(y["age"])


#  Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
x =   { "name":"John", "age":30, "city":"New York"}          # a Python object (dict):
y = json.dumps(x)                                            # convert into JSON:
print(y)

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
"""

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON

dict	Object
list	Array
tuple	Array
str	    String
int  	Number
float	Number
True	true
False	false
None	null
"""

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)                           # convert into JSON:
print(y)                                    # the result is a JSON string:
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True)) 

