# Join Sets
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) 
print(z)

# Join set1 and set2 into a new set:
set1={1,2,3}
set2={4,5,"d"}
set3=set1.union(set2)
print(set3)

set1={1,2,3}
set2={"a","b","c"}
set3=set1 | set2
print(set3)

"""
Code	                Meaning
set1.union(set2)	    Union
set1 | set2	            Union
set1 & set2	            Intersection
set1 - set2	            Difference
set1 ^ set2	            Symmetric difference
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
# myset = set1 | set2 | set3 |set4

# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# intersection_update() - 
# method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# difference_update() method to keep only the items from the first set that are not present in the other set:
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


#  frozenset-immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# set → can change 🔄 
# frozenset → cannot change 🔒

# copy()	 	    Returns a shallow copy	
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

# difference()	-	Returns a new frozenset with the difference
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)
	
# intersection()	&	Returns a new frozenset with the intersection
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)
	
# isdisjoint()	 	Returns True if there is NO intersection between two frozensets	
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

# symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)

# union()	|	Returns a new frozenset containing the union	
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)

"""
add()	 	                  Adds an element to the set
clear()	 	                  Removes all the elements from the set
copy()	 	                  Returns a copy of the set
difference()	-	          Returns a set containing the difference between two or more sets
difference_update()	-=	      Removes the items in this set that are also included in another, specified set
discard()	 	              Remove the specified item
intersection()	&	          Returns a set, that is the intersection of two other sets
intersection_update()	&=	  Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	          Returns True if NO items of this set is present in another set
issubset()	<=	              Returns True if all items of this set is present in another set
 	<	                      Returns True if all items of this set is present in another, larger set
issuperset()	>=	          Returns True if all items of another set is present in this set
 	>	                      Returns True if all items of another, smaller set is present in this set
pop()	 	                  Removes an element from the set
remove()	 	              Removes the specified element
symmetric_difference()	^	  Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	                  Return a set containing the union of sets
update()	|=	              Update the set with the union of this set and others.                 
"""

# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"
colors.discard("green")
# Print the number of items
print(len(colors))