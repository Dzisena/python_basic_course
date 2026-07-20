contacts = {}

try:
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line != "":
                data = line.split(":")
                contacts[data[0]] = data[1]

except FileNotFoundError:
    print("Телефонна книга ще не створена.")
    print("Вона створиться після додавання першого контакту.")


while True:
    print()
    print("=" * 30)
    print("      ТЕЛЕФОННА КНИГА")
    print("=" * 30)
    print("1. Показати всі контакти")
    print("2. Додати контакт")
    print("3. Знайти контакт")
    print("4. Змінити контакт")
    print("5. Видалити контакт")
    print("0. Вийти")
    print("=" * 30)

    choice = input("Оберіть дію: ")

    if choice == "1":
        print()
        print("Список контактів:")

        if len(contacts) == 0:
            print("Телефонна книга порожня.")
        else:
            for name in contacts:
                print(name, "-", contacts[name])

    elif choice == "2":
        print()
        name = input("Введіть ім'я: ").strip()
        phone = input("Введіть номер телефону: ").strip()

        if name == "" or phone == "":
            print("Ім'я та номер не можуть бути порожніми.")

        elif name in contacts:
            print("Контакт з таким ім'ям вже існує.")

        else:
            contacts[name] = phone

            with open("phonebook.txt", "w", encoding="utf-8") as file:
                for person in contacts:
                    file.write(person + ":" + contacts[person] + "\n")

            print("Контакт успішно додано.")

    elif choice == "3":
        print()
        name = input("Введіть ім'я для пошуку: ").strip()

        if name in contacts:
            print("Контакт знайдено:")
            print(name, "-", contacts[name])
        else:
            print("Контакт не знайдено.")

    elif choice == "4":
        print()
        name = input("Введіть ім'я контакту: ").strip()

        if name in contacts:
            print("Поточний номер:", contacts[name])

            new_phone = input("Введіть новий номер: ").strip()

            if new_phone == "":
                print("Номер не може бути порожнім.")
            else:
                contacts[name] = new_phone

                with open("phonebook.txt", "w", encoding="utf-8") as file:
                    for person in contacts:
                        file.write(person + ":" + contacts[person] + "\n")

                print("Контакт успішно змінено.")
        else:
            print("Контакт не знайдено.")

    elif choice == "5":
        print()
        name = input("Введіть ім'я контакту для видалення: ").strip()

        if name in contacts:
            answer = input("Ви точно хочете видалити контакт? так/ні: ")

            if answer.lower() == "так":
                del contacts[name]

                with open("phonebook.txt", "w", encoding="utf-8") as file:
                    for person in contacts:
                        file.write(person + ":" + contacts[person] + "\n")

                print("Контакт видалено.")
            else:
                print("Видалення скасовано.")
        else:
            print("Контакт не знайдено.")

    elif choice == "0":
        print()
        print("Роботу програми завершено.")
        break

    else:
        print()
        print("Такої команди немає. Спробуйте ще раз.")