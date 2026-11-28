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



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for i in range(n):
    word = input()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())



from collections import deque

d = deque()
d.append(1)
print(d)

d.appendleft(2)
print(d)

d.clear()
print(d)

d.extend('1')
print(d)

d.extendleft('234')
print(d)

d.count('1')
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend('7896')
print(d)

d.remove('2')
print(d)

d.reverse()
print(d)

d.rotate(3)
print(d)




from collections import deque

d = deque()

n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == "append":
        d.append(int(command[1]))

    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))

    elif command[0] == "pop":
        d.pop()

    elif command[0] == "popleft":
        d.popleft()

print(*d)




from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            possible = False
            break

        last = current

    if possible:
        print("Yes")
    else:
        print("No")


from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, freq in result[:3]:
        print(char, freq)