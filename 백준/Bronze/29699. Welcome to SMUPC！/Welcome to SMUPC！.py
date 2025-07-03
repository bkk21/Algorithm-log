n = int(input())

st = "WelcomeToSMUPC"

if n >= len(st):
    st = st * (n // len(st) + 1)

print(st[n - 1])