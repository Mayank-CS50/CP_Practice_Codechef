import sys
input=sys.stdin.readline
t=int(input())

def fun(n,x,arr):
    maxx_L=float('-inf')
    for i in range(n-1):
        temp=abs(arr[i]-arr[i+1])
        if temp>maxx_L:
            maxx_L=temp
    
    return max(arr[0],max(maxx_L,2*(x-arr[-1])))
        
for _ in range(t):
    n,x=map(int,input().split())
    L=list(map(int,input().split()))
    print(fun(n,x,L))