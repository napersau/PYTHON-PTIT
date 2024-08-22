for _ in range(int(input())) :
    s = input()
    s = list(s)
    a = ""
    for i in range(len(s) - 1, 0, -1 ) :
        if s[i] >= '5':
            a = a + '0'
            s[i - 1] = str(int(s[i - 1]) + 1)
        else :
            a = a + '0'
            
    a = s[0] + a
    print(a)