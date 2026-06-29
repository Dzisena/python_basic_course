def common_elements():
    numbers_3 = set(range(0, 100, 3))
    numbers_5 = set(range(0, 100, 5))

    result = numbers_3 & numbers_5

    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("OK")
print("Спільні елементи множин:", common_elements())