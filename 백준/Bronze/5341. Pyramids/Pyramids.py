while True:
    n = int(input())

    if n == 0:
        break

    print(sum([x for x in range(1, n+1)]))