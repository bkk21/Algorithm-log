import sys

n = int(input())

rick = ["Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you",
        "Never gonna stop"]

tr = "No"

for _ in range(n):
    m = input()

    if m not in rick:
        tr = "Yes"
        break

print(tr)