# Дан список размера N. Осуществить сдвиг элементов списка влево на одну
# позицию (при этом AN перейдет в AN-1, AN-1 — в AN-2, .., A2 — в A1, a
# исходное значение первого элемента будет потеряно). Последний элемент
# полученного списка положить равным 0.

n = int(input('Введите количество элементов списка: '))
a = ['x'] * n

print('Заполнение списка а:')
i = 0
while i != n:
    a[i] = int(input('Введите число: '))
    i += 1

i = 0
while i != n - 1:  # сдвиг элементов влево
    a[i] = a[i + 1]
    i += 1

a[n - 1] = 0  # изменение последнего элемента
print(a)
