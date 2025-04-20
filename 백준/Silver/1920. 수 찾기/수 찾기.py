import bisect

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()

m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:

    if bisect.bisect_left(nlist, i) != n and nlist[bisect.bisect_left(nlist, i)] == i:
        print("1")
    else:
        print("0")