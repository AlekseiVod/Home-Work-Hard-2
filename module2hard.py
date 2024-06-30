import random


def numeric_field():
    first_field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_field_1 = random.choice(first_field)
    return first_field_1


n = numeric_field()
result = []

for i in range(1, n):
    for j in range(1, n):
        if i < j and i != j and n % (i + j) == 0:
            result.append(i)
            result.append(j)
            continue

print('Число в первом поле', n)
print('Код от двери ', *result, sep='')
