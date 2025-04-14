n, m = map(int, input().split())

answer = list(range(1, n+1))

for i in range(m):
    j, k = map(int, input().split())

    answer[j - 1], answer[k - 1] = answer[k - 1], answer[j - 1]

for i in answer:
    print(i, end=' ')