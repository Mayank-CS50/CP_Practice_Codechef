import sys
input=sys.stdin.readline

def fun(n,A):
    bada=max(A)
    # freq=A.count(bada)
    B,C=[],[]
    for i in A:
        if i!=bada:
            B.append(i)
        else:
            C.append(i)
    if len(B) and len(C):
        print(len(B), len(C))
        print(' '.join(map(str,B)) )
        print(' '.join(map(str,C)) )
    else:
        print(-1)
        
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    fun(n,A)