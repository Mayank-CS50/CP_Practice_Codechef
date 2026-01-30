n=int(input())
rows=[list(map(int,input().split())),list(map(int,input().split())),list(map(int,input().split()))]
col=[]

poi=0
for i in range(n):
    for j in rows:
        col[i][poi]=j[i]
        poi+=1
    


print(rows,col)