with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

bad_word = input("Введіть заборонене слово: ")

count = 0

words = text.split()

for i in range(len(words)):
    clean_word = words[i].strip(".,!?;:\"'()")

    if clean_word.lower() == bad_word.lower():
        words[i] = words[i].replace(clean_word, "*" * len(clean_word))
        count += 1

new_text = " ".join(words)

print("\nНовий текст:\n")
print(new_text)

print("\nСтатистика:")
print("Замінено", count, "слів.")

with open("result3.txt", "w", encoding="utf-8") as file:
    file.write(new_text)