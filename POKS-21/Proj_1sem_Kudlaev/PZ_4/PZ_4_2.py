# Дано целое число N (> 1). Найти наименьшее целое число K,
# при котором выполняется неравенство 3^К > N

n = input('Введите n: ')

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        n = input('Нужно ввести целое число n: ')

while n <= 1:  # обработка исключений
    n = int(input('Нужно ввести число n > 1: '))

k = 0

while 3 ** k <= n:  # поиск подходящего числа
    k += 1

print('Наименьшее такое число =', k)
