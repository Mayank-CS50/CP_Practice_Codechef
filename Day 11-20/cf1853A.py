import sys
import math
input=sys.stdin.readline

def fun(n,A):
    if sorted(A)!=A:
        return 0
    else:
        chota_diff=float('inf')
        for i in range(n-1):
            if abs(A[i]-A[i+1])<chota_diff:
                chota_diff=abs(A[i]-A[i+1])
            print(chota_diff,'jj')
        temp=chota_diff/2
        if temp==1:
            return 1
        else:
            return (chota_diff//2)+1
     
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    print(fun(n,A))