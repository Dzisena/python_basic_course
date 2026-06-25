number = int(input("Введіть число: "))

while number > 9:
    result = 1
    text = ""

    for i in str(number):
        result = result * int(i)
        text = text + i + " * "

    text = text[:-3]

    print(text, "=", result)

    number = result

print("Результат:", number)