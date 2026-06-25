import string

letters = string.ascii_letters

text = input("Введіть діапазон букв через дефіс: ")

first_letter, second_letter = text.split("-")

start = letters.index(first_letter)
finish = letters.index(second_letter)

answer = letters[start:finish + 1]

print("Результат:", answer)