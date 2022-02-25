# Дано целое число N (>0)
# Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)
import tkinter as tk


def func():
    N = int(entry_1.get())

    while type(N) != int:  # обработка исключений
        try:
            N = int(N)
        except ValueError:
            N = input('Нужно ввести целое число n: ')

    while N <= 0:  # обработка исключений
        N = int(input('Нужно ввести число n > 0: '))

    i = 1  # счетчик
    p = 1  # результат

    while i != N + 1:  # вычисление произведения
        p *= 1 + 0.1 * i
        i += 1
    label.config(text="Произведение: {}".format(p))

root = tk.Tk()
entry_1 = tk.Entry(root)
entry_1.pack()
label = tk.Label(root, text="Введите числа:")
label.pack()
button = tk.Button(root, text='Получить произведение', command=func)
button.pack()
root.mainloop()
