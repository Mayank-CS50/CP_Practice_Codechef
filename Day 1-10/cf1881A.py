import sys
input = sys.stdin.readline
t= int(input())

def fun(x,s):
    n=0
    if s in x:
        return 0
    while True:
        x+=x
        n+=1
        if s in x:
            return n
        elif len(x) > len(s)*2:
            break
    return -1

for _ in range(t):
    n,m = map( int, input().split())
    x = input().strip()
    s = input().strip()
    print( fun(x,s))
    