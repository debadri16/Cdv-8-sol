def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def fibonacci(sa,sb,lgt):
    a1=sa
    b1=sb
    n1=lgt
    #print(a1,b1,n1)
    if n1 < 0: 
        print("Incorrect input") 
    elif n1 == 1: 
        return a1 
    elif n1 == 2: 
        return b1 
    else: 
        for i in range(2,n1): 
            c = a1 + b1 
            a1 = b1 
            b1 = c
        return b1 

x = list(map(str,input().split()))
a=int(x[0])
b=int(x[1])

l1=[]
for i in range(a,b):
    if isPrime(i):
        l1.append(i)

l2=[]
set1=set()
for i in l1:
    for j in l1:
        if i != j:
            s=str(i)+str(j)
            set1.add(int(s))
for i in set1:
    if isPrime(i):
        l2.append(i)

if len(l2)==0:
    sa=0
    sb=0
else:
    #print(l2)
    sa=min(l2)
    sb=max(l2)
lgt=len(l2)
#print(lgt)

anss=fibonacci(sa,sb,lgt)

if len(l2)==0:
    print('',end='')
else:
    print(anss,end='')
