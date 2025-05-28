
m = input()

if m == "Later!":
    print("Alligator!")

m = m[0] + (m[1:-1] * 2) + m[-1]
print(m)