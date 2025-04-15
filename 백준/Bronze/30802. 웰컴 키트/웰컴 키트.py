n = int(input())

numlist = list(map(int, input().split()))

t, p = map(int, input().split())

tsum = 0

for i in numlist:

    tsum += i // t
    i = i % t

    if i != 0:
        tsum += 1
        
print(tsum)
print(n//p, n%p)