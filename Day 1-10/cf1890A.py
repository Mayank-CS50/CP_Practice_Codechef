import sys
input = sys.stdin.readline
t= int(input())

def fun( n, A):
    temp_set=set(A)
    if len(temp_set)>2:
        return 'No'
    if len(temp_set)==1:
        return 'Yes'
    A.sort()
    f1=A.count(A[0])
    f2=A.count(A[-1])
    if n%2==0:
        if f1==f2:
            return 'Yes'
    else:
        if f1==f2+1 or f1+1==f2:
            return 'Yes'
    return 'No'


        #JUST TRIED, ANOTHER WAY IT DIDN'T WORKKKK XD
    # dic={}
    # for i in range(n):
    #     if i not in dic:
    #         dic[i]=1
    #     else:
    #         dic[i]+=1
    
    # if len(dic)==2:
    #     val=list(dic.values())
    #     print(val[0])
    #     if n%2==0:
    #         if val[0]==val[1]:
    #             return 'Yes'
    #     else:
    #         if val[0]==val[1]+1 or val[0]+1==val[1]:
    #             return 'Yes'
    # elif len(dic)>2:
    #     return 'No'
    # else:
    #     return 'Yes'
    # return 'No'
    
            
        

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print( fun(n,A))

