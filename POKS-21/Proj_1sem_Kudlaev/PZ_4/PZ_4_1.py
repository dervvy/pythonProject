# Дано целое число N (>0)
# Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)

n = input('Введите n: ')

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        n = input('Нужно ввести целое число n: ')

while n <= 0:  # обработка исключений
    n = int(input('Нужно ввести число n > 0: '))

i = 1  # счетчик
p = 1  # результат

while i != n + 1:  # вычисление произведения
    p *= 1 + 0.1 * i
    i += 1

print('Результат произведения =', p)