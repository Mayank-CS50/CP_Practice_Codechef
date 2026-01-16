import sys
input = sys.stdin.readline
t = int(input())

def fun(n, k, A):
    if k in A:
        return 'YES'
    return 'NO'

for _ in range(t):
    n, k = map( int,input().split())
    A = list(map( int,input().split()))
    print( fun(n,k,A))