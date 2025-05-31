import sys
from collections import Counter

n = int(input())

nlist = [ int(sys.stdin.readline()) for _ in range(n) ]

nlist.sort()

#산술평균
print(round(sum(nlist) / n))

#중앙값
print(nlist[n // 2])

#최빈값
c = dict(Counter(nlist))
k = [x for x, y in c.items() if y == max(c.values())]
if len(k) >= 2:
    print(k[1])
else:
    print(k[0])

#범위
print(max(nlist) - min(nlist))