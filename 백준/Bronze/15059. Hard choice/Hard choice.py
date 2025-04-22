a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

nlist = []

if b1 - a1 > 0:
    nlist.append(b1 - a1)
if b2 - a2 > 0:
    nlist.append(b2 - a2)
if b3 - a3 > 0:
    nlist.append(b3 - a3)

print(sum(nlist))