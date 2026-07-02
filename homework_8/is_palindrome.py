def is_palindrome(text):
    text = "".join(i.lower() for i in text if i.isalnum())
    return text == text[::-1]


text = input("Введіть текст: ")

if is_palindrome(text):
    print(True)
else:
    print(False)

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False

print("OK")