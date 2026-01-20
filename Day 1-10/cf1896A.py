import sys
input=sys.stdin.readline
t=int(input())

def fun(arr):
    if arr[0]==1:
        return 'YES'
    return 'NO'

for _ in range(t):
    n=int(input())
    L=list(map(int,input().split()))
    print(fun(L))