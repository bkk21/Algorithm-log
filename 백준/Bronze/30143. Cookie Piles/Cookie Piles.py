n = int(input())

for i in range(n):

    n, a, d = map(int, input().split())

    count = a
    mid = a
    for _ in range(n - 1):
        mid += d
        count += mid

    print(count)
    