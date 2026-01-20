import sys
input = sys.stdin.readline
t = int(input())

def fun(n,A):
    return -(sum(A))

for _ in range(t):
    n = int(input())
    L = list( map (int, input().split()))
    print( fun(n, L))