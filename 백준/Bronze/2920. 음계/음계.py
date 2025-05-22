import sys, re

input = sys.stdin.readline

x = re.sub(r"\s", "", input())

if x == '12345678':
    print("ascending")
elif x == "87654321":
    print("descending")
else:
    print("mixed")
