n = int(input())

money = [25, 10, 5, 1]

for _ in range(n):
    now = int(input())

    for i in money:
        print(now // i, end = ' ')
        now = now % i
     
    print()