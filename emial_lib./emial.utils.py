import email.utils
import re

n = int(input())
for i in range(n):
    N,e = email.utils.parseaddr(input())
     
    if re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',e):
        print(email.utils.formataddr((N,e)))