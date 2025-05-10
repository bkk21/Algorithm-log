n, k = map(int, input().split())

nlist = []
for _ in  range(n):
    nlist.append(int(input()))

count = 0

for i in nlist[::-1]:
    count += k // i
    k = k % i

print(count)