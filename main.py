number = int(input('Введите число: '))
i = 0
element = 1
while i < number:
    element *= (i + 1)
    print(element)
    i += 1
