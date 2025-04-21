n = int(input())

nlist = []

for i in range(n):
    m = int(input())

    if m == 0:
        nlist.pop()
    else:
        nlist.append(m)

print(sum(nlist))