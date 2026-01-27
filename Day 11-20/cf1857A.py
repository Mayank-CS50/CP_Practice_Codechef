for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    odd_count=0
    for i in A:
        if i%2!=0:
            odd_count+=1
    if odd_count%2==0:
        print('YES')
    else:
        print('NO')