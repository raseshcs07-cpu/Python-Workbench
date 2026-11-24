from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))

print(Counter(myList).items())

print(Counter(myList).keys())

print(Counter(myList).values())



x = int(input())
s_s = list(map(int, input().split()))
n = int(input())

customers = []
for i in range(n):
    s, price = map(int, input().split())
    customers.append((price, s))  # Price ko pehle rakha hai taaki sort aasani se ho

# Price ke hisaab se bade se chhote (descending) order mein sort karein
customers.sort(reverse=True)

a = 0
for price, s in customers:
    if s in s_s:
        a += price
        s_s.remove(s)

print(a)



x = int(input())
s_s = list(map(int, input().split()))
n = int(input())

a = 0
for i in range(n):
    s, price = map(int, input().split()) 

    if s in s_s:
        a += price
        s_s.remove(s)
         
print(a)





from collections import Counter

x = int(input())
shoes = Counter(map(int, input().split()))  # Har size ke kitne joote hain, count karega
n = int(input())

customers = []
for _ in range(n):
    size, price = map(int, input().split())
    customers.append((price, size))

# Price ke hisaab se descending order (zyada se kam) mein sort karein
customers.sort(reverse=True)

total_earned = 0
for price, size in customers:
    if shoes[size] > 0:  # Check karein ki us size ka stock bacha hai ya nahi
        total_earned += price
        shoes[size] -= 1  # Stock mein se 1 joota kam kar dein

print(total_earned)


from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print (i)




from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)

for i in range(n):
    word = input()
    d[word].append(i+1)
    
for i in range(m):
    word = input()
    
    if word in d:
        print(*d[word])
    else:
        print(-1)


from collections import namedtuple

Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print (xyz)

Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print (xyz.Class)



from collections import namedtuple

Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print (dot_product)




from collections import namedtuple

n = int(input())

Student = namedtuple('Student', input())

total = 0

for i in range(n):
    data = input().split()
    s = Student(*data)
    total += int(s.MARKS)

print(f"{total / n:.2f}")



from collections import OrderedDict

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5
print(ordinary_dictionary)


from collections import OrderedDict

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5
print(ordinary_dictionary)




from collections import OrderedDict

n = int(input())

items = OrderedDict()

for i in range(n):
    data = input().split()
    
    name = " ".join(data[:-1])
    price = int(data[-1])

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)

