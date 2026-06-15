price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть знижку на товар: "))

new_price = (price * discount / 100)
result = price - new_price
print("Знижка:", new_price)
print("Нова ціна товару: ", result)