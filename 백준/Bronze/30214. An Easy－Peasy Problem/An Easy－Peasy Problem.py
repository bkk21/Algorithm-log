import sys
a, b = map(int, sys.stdin.readline().split())

if a >= b / 2:
    print("E")
else:
    print("H")