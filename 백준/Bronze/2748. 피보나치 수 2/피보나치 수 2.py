d = [0] * 91
d[1] = 1
d[2] = 1

n = int(input())

def f(x):
    if x == 1 or x == 2:
        return 1

    if d[x] == 0:
        d[x] = d[x - 1] + d[x - 2]
        
    return d[x]

for i in range(2, n+1):
    f(i)

print(d[n])