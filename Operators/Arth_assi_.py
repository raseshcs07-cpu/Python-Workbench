s1 = 100+150
s2=s1+99
s3=s2+98
print(s1)
print(s2)
print(s3)

"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
"""

x=2
y=5
print(x ** y)

x = 15
y = 2
print(x // y)

x = 5
y = 2
print(x % y)

# / - Division (returns a float)
# // - Floor division (returns an integer)

"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)
"""

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)
"""
and Gate logic
"""

x = 5
x |= 3
print(x)
"""
Binary conversion:
9
Keep dividing by 2 and write the remainder:
9 ÷ 2 = 4  remainder 1
4 ÷ 2 = 2  remainder 0
2 ÷ 2 = 1  remainder 0
1 ÷ 2 = 0  remainder 1
Now read the remainders from bottom to top:
1001

0110
Binary:     0    1    1    0
Position:   3    2    1    0
Value:     2³   2²   2¹   2⁰

0 × 2³ = 0 × 8 = 0
1 × 2² = 1 × 4 = 4
1 × 2¹ = 1 × 2 = 2
0 × 2⁰ = 0 × 1 = 0
0 + 4 + 2 + 0 = 6
6
"""
x = 5
x ^= 3
print(x)
"""XOR rule"""

x = 5
x >>= 3
print(x)
"""

{m1}
5 = 0101
Now >> 3 means move everything 3 places to the right.
0101 >> 3
   ↓↓↓
0000
0  1  0  1
         → 1
      → 0
   → 1
After moving 3 places, nothing is left:
0  0  0  0


{m2}
For positive numbers, each >> 1 divides by 2:

5 >> 1  →  5 ÷ 2 = 2
2 >> 1  →  2 ÷ 2 = 1
1 >> 1  →  1 ÷ 2 = 0
Therefore:
5 >> 3 = 0
So >> 3 means shift right 3 times.
"""

x = 5
x <<= 3
print(x)
"""
0101 << 1  → 1010
1010 << 1  → 10100
10100 << 1 → 101000

5 << 1 = 10
5 << 2 = 20
5 << 3 = 40
"""

print(x := 99)

# walrus operator
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"\n\nList has {count} elements")

# Ternery operator
num=6
x="Weekend " if num > 5 else "Workday"
print(x)

num=int(input("Enter your value:"))                                                           #int age;
x = "Fri" if num == 5 else "Sat" if num == 6  else "Sun" if  num == 7  else  " weekday"    #scanf("%d", &age);
print(x)


#include <stdio.h>
"""
int main() {
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Your age is %d", age);

    return 0;
}"""