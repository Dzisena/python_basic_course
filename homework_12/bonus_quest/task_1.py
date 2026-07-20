with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

with open("result1.txt", "w", encoding="utf-8") as file:
    for word in words:
        word = word.strip(".,!?;:\"'()")
        if len(word) >= 7:
            file.write(word + "\n")

print("Готово!")