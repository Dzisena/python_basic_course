number = int(input("Введіть кількість секунд: "))

days = number // 86400

number = number % 86400

hours = number // 3600

number = number % 3600

minutes = number // 60

seconds = number % 60


if days % 10 == 1 and days != 11:
    day_text = "день"
elif 2 <= days % 10 <= 4:
    day_text = "дні"
else:
    day_text = "днів"


hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(days, day_text + ",", hours + ":" + minutes + ":" + seconds)