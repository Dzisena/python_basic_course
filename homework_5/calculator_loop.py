while True:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    action = input("Введіть дію (+, -, *, / ): ")

    if action == "+":
        print("Результат: ", num1 + num2)

    elif action == "-":
        print("Результат: ", num1 - num2)

    elif action == "*":
        print("Результат: ", num1 * num2)

    elif action == "/":
        print("Результат: ", num1 / num2)

    else:
        print("Невідома Операція!!! ")

    answer = input("Продовжити? (y/n): ")

    if answer == "n":
        break