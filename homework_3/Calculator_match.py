num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
action = input("Введіть дію (+, -, *, / ): ")

match action:
    case "+":
        print('Результат: ',num1 + num2)
    case "-":
        print("Результат: ", num1 - num2)
    case "*":
        print("Результат: ", num1 * num2)
    case "/":
        print("Результат: ", num1 / num2)
    case _:
        print("Невідома операція!!!")