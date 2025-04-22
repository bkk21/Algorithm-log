dic = {'-':0, '(': 2, '@': 3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    n = input()
    n = n[::-1]
    m = 0
    sum = 0

    if n == '#':
        break
    
    for i in n:
        try:
            sum += (8**m) * dic[i]
        except:
            sum += (8**m)
        m += 1

    print(sum)