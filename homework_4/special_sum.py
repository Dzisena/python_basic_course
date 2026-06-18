lists = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for sum in lists:
    if len(sum) == 0:
        result = 0
    else:
        sum_even_index = 0

        for i in range(0, len(sum), 2):
            sum_even_index += sum[i]

        result = sum_even_index * sum[-1]

    print(sum, "->", result)