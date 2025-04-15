import math
a, b = map(int, input().split())

for j in range(a, b+1):
    if j > 1 and all(j % i != 0 for i in range(2, int(math.sqrt(j)) + 1)):
        print(j)