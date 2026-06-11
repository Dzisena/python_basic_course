price = int(input("Введіть ціну товару: "))
discount = int(input("Введіть знижку на товар: "))

new_price = (price * discount/100)
print("Нова ціна товару: ", new_price)