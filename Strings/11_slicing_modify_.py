a = "\nHello"
print(a)

# Multiline strings
a = """ \nMy name is Rasesh ,       
I am btech cse student ,
learning python.\n"""
print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[1]) 
print(a[8],"\n")

# for loop
for x in " Rushace":
    print(x)

a= "Hello Rushace"
print(len(a))

txt = "I will watch Game of thrones from this weekend. "
print("\n","weekend" in txt)

# if statement 

a = "I will watch Game of thrones from this weekend."
if "weekend" in a:
    print("\nyes ,  weekend is present\n ")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("\nNo, 'expensive' is NOT present.")



#  Slicing 
#  - return a range of characters

a = "Hey Rasesh"
print(a[5:8])
print(a[:5])
print(a[-5:-2])


#  Modify

a = "Hey Rasesh. "
print(a.upper())
print(a.lower())
print(a.strip())          # removes any whitespace from the beginning or the end
print(a.replace("H","J"))
print(a.split(","))

