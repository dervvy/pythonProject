# В последовательности на n целых чисел найти и вывести:
# 1. минимальный среди положительных
# 2. элементы кратные пяти
# 3. их среднее арифметическое

from random import randint
n = [randint(-9, 9) for i in range(int(input('Введите количество чисел в последовательности: ')))]
print(n)
print(max([i for i in n if i > 0]), '\n' + str([i for i in n if i % 5 == 0]), '\n' + str(sum(n)/len(n)))
