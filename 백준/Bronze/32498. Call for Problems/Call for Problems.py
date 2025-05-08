n = int(input())

count = 0

for _ in range(n):
    if int(input()) % 2 != 0:
        count += 1

print(count)