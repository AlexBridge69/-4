# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
number = int(input('Введите число: '))
i = 0
element = 1
while i < number:
    element *= (i + 1)
    print(element)
    i += 1