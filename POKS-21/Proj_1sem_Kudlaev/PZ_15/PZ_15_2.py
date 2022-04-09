# В матрице найти сумму элементов второй половины матрицы

from random import randint

a = int(input('Введите количество строк матрицы: '))
b = int(input('Введите количество столбцов матрицы: '))

# создание матрицы
C = [0] * a

print('\nВаша матрица:')
for i in range(a):
    C[i] = [0] * b

for i in range(a):
    for k in range(b):
        C[i][k] = randint(-10, 10)
        if k == b-1:
            print(C[i])

# подсчет суммы элементов второй половины матрицы
d = 0
print('\nВторая половина матрицы:')
for i in range(round(a/2), a):
    for k in range(b):
        d += int(C[i][k])
        if k == b-1:
            print(C[i])

print('\nСумма элементов второй половины матрицы =', d)