#CF431A

A=list(map(int,input().split()))
s=input()
cal=0
for i in s:
    var=int(i)
    cal+=A[var-1]
print(cal)

"""
Fundamental argument of ours will be,
ith number of strip ki occourance frequency ko simply multiply kardo ussi ke amount of respective calories se """
