import itertools

n, m = map(int, input().split())

numlist = list(map(int, input().split()))

nCr = itertools.combinations(numlist, 3)

answer = 0

for i in nCr:

    tp = sum(list(i))

    if tp <= m and tp > answer:
        answer = tp

print(answer)
    