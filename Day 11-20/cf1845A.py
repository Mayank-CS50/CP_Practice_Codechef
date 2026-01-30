for _ in range(int(input())):
    n,k,x=map(int,input().split())
    
    if x==1 and k<2:
        print('NO')
    elif n%2!=0 and x==1:
        print('NO')
    else:
        print('YES')
        print(n)
        print('1 '*n)