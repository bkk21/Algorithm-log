from collections import Counter
n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

q = Counter(nlist)

for i in mlist:
    print(q[i], end= ' ')