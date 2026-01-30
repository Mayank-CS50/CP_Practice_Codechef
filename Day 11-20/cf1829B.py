for _ in range(int(input())):
    count = 0
    n=int(input())
    s=list(map(int,input().split()))
    maxx=float('-inf')
    for i in s:
        # print(i,count,maxx)
        if i==1:
            count=0
        else:
            count+=1
        if count>maxx:
            maxx=count
    print(maxx)
    
