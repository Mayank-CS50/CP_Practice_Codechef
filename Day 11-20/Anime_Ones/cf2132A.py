#CF2132A

for _ in range(int(input())):
    n=int(input())
    a=input()
    m=int(input())
    b=input()
    c=input()
    req=a
    poi=0
    for i in c:
        if i=='V':
            req=b[poi]+req
        else:
            req+=b[poi]
        poi+=1
    print(req)
    
#Simple Brute force, no big deal just read the ques