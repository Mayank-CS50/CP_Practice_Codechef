import sys
input = sys.stdin.readline
t = int( input())

def fun(n):
    if n % 3 == 0:
        return 'Second'
    return 'First'

for _ in range(t):
    n = int( input())
    print( fun(n))