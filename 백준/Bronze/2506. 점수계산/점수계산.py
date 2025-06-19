n = int(input())

nlist = list(map(int, input().split()))

se = 0

count = 0

count += nlist[0]

if nlist.pop(0) != 0:
    se += 1

for i in nlist:
    if i != 0:
        se += 1
        count += se
    else:
        se = 0
        count += i

print(count)