from collections import deque
n = int(input())

nlist = deque([])

for _ in range(n):
    nlist.append(input())

count = 0

for _ in range(n):
    m = input()

    if m == nlist[0]:
        nlist.popleft()
    else:
        count += 1
        nlist.remove(m)

print(count)