def ucln(a, b):
    if b == 0 :
        return a
    else:
        return ucln(b, a % b)

def snt( n) :
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for  _  in range(int(input())) :
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if ucln(n, i) == 1 :
            cnt += 1
    if snt(cnt) == 1 :
        print("YES")
    else :
        print("NO")
    
