import sys
input=sys.stdin.readline

def fun():
    L=[]
    count=0
    for _ in range(10):
        L.append(list(input().strip()))
    for i in range(10):
        for j in range(10):
            if L[i][j]=='X':
                n,m=i,j
                if n > 4:
                    n = 9 - i
                if m > 4:
                    m = 9 - j 
                # print(i,j,n,m)
                
                count+=min(n, m) + 1
            #print (1 + 1, j + 1)
    return count

t=int(input())
for _ in range(t):
    print(fun())