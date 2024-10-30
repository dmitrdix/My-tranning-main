n=int(input())
a=int()
b=int()
for a in range(1,20):
    for b in range(1,20):
        if n%(a+b)==0 and a<b:
             print(str(a)+str(b),end='')