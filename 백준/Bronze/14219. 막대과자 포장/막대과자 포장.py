a, b = map(int, input().split())

if a % 3 == 0 and b >= 1:
    print("YES")
elif b % 3 == 0 and a >= 1:
    print("YES")
else:
    print("NO")