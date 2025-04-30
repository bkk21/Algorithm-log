from collections import deque

n = int(input())

nlist = deque(list(range(n, 0, -1)))

while len(nlist) != 1:
    nlist.pop()
    nlist.appendleft(nlist.pop())

print(nlist[0])