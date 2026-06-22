import string
import keyword

name = input("Введіть ім'я змінної: ")

is_correct = True

if name in keyword.kwlist:
    is_correct = False

if name[0] in "0123456789":
    is_correct = False

if name.lower() != name:
    is_correct = False

if "__" in name:
    is_correct = False

for i in name:
    if i in string.punctuation:
        if i != "_":
            is_correct = False

    if i == " ":
        is_correct = False

print(is_correct)