a, b = map(int, input().split())

n = ''
n2 = ''
new = ''

for _ in range(a):
    n += input()

for _ in range(a):
    n2 += input()

for i in n :
    new += i * 2

if new == n2:
    print("Eyfa")
else:
    print("Not Eyfa")