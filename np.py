from string import ascii_uppercase

x=10
d={}
for c in ascii_uppercase:
    d[c]=x
    x+=1

y = list(map(str,input().split()))

def getDec(s,b):
    val=0
    k=0
    for i in range(len(s)-1,-1,-1):
        if s[i].isdigit():
            val+=int(s[i]) * (b**k)
        else:
            val+=d[s[i]] * (b**k)
        k+=1
    return(val)

tmp=0
mm=999999
for i in y:
    x='-1'
    c=','
    for j in i:
        if j.isdigit() and j>x:
            x=j
        elif not (j.isdigit()) and j==',':
            c=j
        elif not (j.isdigit()) and j>c:
            c=j
    if c==',':
        tmp=int(x)+1
    else:
        tmp=d[c]+1
    dec=getDec(i,tmp)
    mm=min(mm,dec)
    #print(dec)

print(mm)
