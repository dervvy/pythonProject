# Дано число R и список A размера N. Найти элемент списка, который наиболее
# близок кчислу R (то есть такой элемент AK, для которого величина |AK - R|
# является минимальной).

n = int(input('Введите количество элементов списка A: '))
r = float(input('Введите число R: '))
a = ['x'] * n

print('Заполнение списка а:')
i = 0
ak = 0
while i != n:
    a[i] = float(input('Введите число: '))
    i += 1

i = 0
k = abs(a[i] - r)
while i != n:  # рассчет значений |AK - R|
    if abs(a[i] - r) < k:
        k = abs(a[i] - r)
        ak = a[i]
    i += 1

print('Элемент списка ближайший к R =', ak)
