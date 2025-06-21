t = int(input())

for _ in range(t):
    n = int(input())

    now_univ = ''
    now_al = 0

    for _ in range(n):
        univ, al = input().split()

        if int(now_al) < int(al):
            now_univ = univ
            now_al = al

    print(now_univ)