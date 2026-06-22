import random

n = random.randint(3, 10)
lst = []
for i in range(n):
    lst.append(random.randint(1, 10))
print("Початковий список: ", lst)

result = []

result.append(lst[0])
result.append(lst[2])
result.append(lst[-2])

print("Результат:  ", result)