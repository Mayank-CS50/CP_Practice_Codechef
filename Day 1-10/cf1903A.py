import sys
input=sys.stdin.readline
t=int(input())

def fun():
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    if k>1 or L==sorted(L):
        return 'YES'
    return 'NO'
for _ in range(t):
    print(fun())