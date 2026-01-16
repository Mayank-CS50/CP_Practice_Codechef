import sys
input = sys.stdin.readline
t= int(input())

def fun(x,s):
    n=0
    while len(x)<=len(s):
        x+=x
        n+=1
        if s in x:
            return n      
    return -1

for _ in range(t):
    n,m=input(),input()
    x,s=input(),input()
    print(fun(x,s))