for _ in range(int(input())): 
    n=int(input())
    A=list(map(int,input().split()))
    
    L=[A[0]]
    for i in range(1,n):
        if A[i]<A[i-1]:
            L.append(A[i])
        L.append(A[i])
    print(len(L))
    print(' '.join(map(str,L)))