import sys

input = sys.stdin.readline

st = input()

for i in st:
    if i.islower():
        print(i.upper(), end = '')
    else:
        print(i.lower(), end = '')