num = int(input("Введіть 4-значне число: "))

num1 = num // 1000
num2 = (num // 100) % 10
num3 = (num // 10) % 10
num4 = num % 10

print(num1, num2, num3, num4, sep="\n")
