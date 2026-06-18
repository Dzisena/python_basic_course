lists = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for arr in lists:
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    for num in arr:
        if num == 0:
            result.append(num)

    print(arr, "\n", result)