t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    nlist = list(map(int, input().split()))
    nlist = [ i // k for i in nlist]

    print(sum(nlist))