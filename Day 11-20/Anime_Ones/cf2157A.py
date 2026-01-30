#CF2157B

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    from collections import Counter
    dic=Counter(A)
    count=0
    for i in dic:
        if dic[i]>i:
            count+=dic[i]-i
        elif dic[i]<i:
            count+=dic[i]
    print(count)

"""
Simplest argument i could think of was,
Agar uss number ki frequency same hai, as that of the number then do nothing
If freq. > number, to excess number delete karne honge, i.e. freq-number
Else freq. < number, then no way exists that it can be fulfilled, thus poori trah hi delete krna hoga uss number ki existance ko,
hence count is +freq.

Done
"""