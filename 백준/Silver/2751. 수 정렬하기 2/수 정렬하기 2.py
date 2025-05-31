import sys

n = int(input())

nlist = [ int(sys.stdin.readline()) for _ in range(n) ]

nlist.sort()

for i in nlist:
    print(i)