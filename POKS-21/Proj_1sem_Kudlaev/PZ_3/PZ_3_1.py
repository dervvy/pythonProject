# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Числа A и B имеют одинаковую четность».

A = input("A= ")
B = input("B= ")

while type(A) != int:  # обработка исключений
    try:
        A = int(A)
    except ValueError:
        A = input("Введите целое число A ")

while type(B) != int:  # обработка исключений
    try:
        B = int(B)
    except ValueError:
        B = input("Введите целое число B ")

if A % 2 == B % 2:
    print("Четность одинаковая")
else:
    print("Четность разная")
