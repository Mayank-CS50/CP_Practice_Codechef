t=int(input())

def fun(n,A):
        total = 0
        temp_c = 0
        for i in A:
                if i == '#':
                    temp_c = 0
                else:
                    total += 1
                    temp_c += 1
                    if temp_c > 2:
                        return 2
        return total
        

for i in range(t):
        n = int(input())
        L = input()
        print(fun(n,L))
        