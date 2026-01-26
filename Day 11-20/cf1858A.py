import sys
input=sys.stdin.readline

def fun(a,b,c):
    if c%2!=0:
        if b>a:
            return 'Second'
        else:
            return 'First'
    else:
        if b>=a:
            return 'Second'
        else:
            return 'First'
        
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(fun(a,b,c))