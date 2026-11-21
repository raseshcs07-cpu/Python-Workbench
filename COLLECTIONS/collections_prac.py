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
