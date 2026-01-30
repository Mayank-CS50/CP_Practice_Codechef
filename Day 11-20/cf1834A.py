for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    pos=A.count(1)
    neg=A.count(-1)
    reg=neg-pos
    print(neg,pos,reg)
    if neg%2==0:
            countt=(0)
    else:
            countt=(1)
    if reg<0:
        print(reg+countt)
    else:
        print(reg)