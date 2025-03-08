num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2 // 10) % 10))
print(num1 * ((num2 // 10) // 10))
print(num1 * num2)