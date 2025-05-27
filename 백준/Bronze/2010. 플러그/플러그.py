import sys

input = sys.stdin.readline
n = int(input())

count = 0

for _ in range(n):
    count += int(input())

print(count - (n - 1))