n, m = map(int, input().split())

answer = [0] * n

for i in range(m):
    i, j, k = map(int, input().split())

    for p in range(i-1, j):
        answer[p] = k

for i in answer:
    print(i, end=' ')