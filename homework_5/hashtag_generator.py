import string

text = input("Введіть текст: ")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

hashtag = "#" + text.title().replace(" ", "")

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)