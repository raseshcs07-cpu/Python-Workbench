from itertools import product

print (list (product ( [1,2,3] , repeat = 2 )),"\n")

print (list (product ( [1,2,3] , [3,4] )),"\n")

A = [[1,2,3],[3,4,5]]
B = [[1,2,3],[3,4,5],[7,8]]
print (list (product (*A) ),"\n")
print (list (product (*B) ),"\n")

r = list (product (A,B) )
print(*r,"\n")
print(*product (A, B) ,"\n")

from itertools import permutations
print(permutations (['1','2','3']) ,"\n")
print (list (permutations (['1','2','3'] )),"\n")
print (list( permutations (['1','2','3'],2 )),"\n")
print (list (permutations ('abc',3 )),"\n")


from itertools import permutations
S,s = input().split()
s = int(s)

for i in sorted(permutations(S,s)):
    print(''.join(i))