n,m=map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(input())

encountered=False
countt=0
for i in range(n):
    val1=mat[i]
    for j in range(m):
        
        val=val1[j]
        if not encountered and val=='B':
            encountered=True
            col=j+1
            row=i+1
            countt=1
        elif val=='B':
            countt+=1
    if encountered:
        break
# print(countt,row,col)
length=countt
reqd=(length-1)//2
print(row+reqd, col+reqd)
