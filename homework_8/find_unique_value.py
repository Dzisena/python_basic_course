def find_unique_value(some_list):
    for i in some_list:
        if some_list.count(i) == 1:
            return i


numbers = list(map(float, input("Введіть числа через пробіл: ").split()))

print(find_unique_value(numbers))

assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5

print("OK")