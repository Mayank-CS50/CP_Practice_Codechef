#CF2167A

for _ in range(int(input())):
    n=int(input())
    s,t=input().split()
    if sorted(s)==sorted(t):
        print('YES')
    else:
        print('NO')
        
'''Anagram ka question, simple <bcz i'mma python ;_;'''
    # d1,d2={},{}
    # for i in range(n):
    #     if s[i] in d1:
    #         d1[s[i]]+=1
    #     else:
    #         d1[s[i]]=1
    #     if t[i] in d2:
    #         d2[t[i]]+=1
    #     else:
    #         d2[t[i]]=1
          
    # found=True  
    # for j in d1:
    #     try:
    #         if d1[j]==d2[j]:
    #             continue
    #         else:
    #             found=False
    #             break
    #     except:
    #             found=False
    #             break
    # if not found:
    #     print('NO')
    # else:
    #     print('YES')
            