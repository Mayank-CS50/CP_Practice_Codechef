#CF2149A

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    t1=A.count(0)
    t2=A.count(-1)
    if t2%2==0:
        print(t1)
    else:
        print(t1+2)
        
        
'So maine ye observe kara 2 tries ke baad,'
'''That if -1 parity is odd, to product will be -negative hamesha, and vice versa ke liye opposite.
On the other hand, 0's ko to anyhow +1 karna hi hai, to make the overall product strictly +ve, i.e. >0
So count of 0s and -1s in t1 and t2, then acc. to -1's, if it's odd, to uss ek -1 ko +ve krne me 2 steps lagenge, -1+1->0+1->+1

Hence, the deduced answer....
'''