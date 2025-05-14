import sys 

input = sys.stdin.readline

nlist = [0] * 10001

n = int(input())

for _ in range(n):
    nlist[int(input())] += 1

for j in range(len(nlist)):
    if nlist[j] != 0:
        for _ in range(nlist[j]):
            print(j)