n, d = map(int, input().split())

leri = {'d':'b', 'b':'d', 'q':'p', 'p':'q'}
updo = {'d':'q', 'b':'p', 'q':'d', 'p':'b'}

for _ in range(n):
    m = input()

    if d == 1:
        for i in m:
            print(updo[i], end='')
        print()
    else:
        for i in m:
            print(leri[i], end='')
        print()