n = int(input())
s = input()

m = ['a', 'e', 'i', 'o', 'u']

count = 0

for i in s:
    if i in m:
        count += 1

print(count)