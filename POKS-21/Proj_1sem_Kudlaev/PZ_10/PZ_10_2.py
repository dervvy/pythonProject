# Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить строку
# наименьшей длины

# вывод текста на экран
f1 = open('text18-11.txt', encoding='utf-8')
t = f1.read()
print(t)
t = list(t)


i = 0
k = 0

# подсчет знаков препинания
while i != len(t):
    if t[i] == '!' or t[i] == ',' or t[i] == '.':
        k += 1
    i += 1

print('\nКоличество знаков препинания: ', k)

f1 = open('text18-11.txt', encoding='utf-8')
l = f1.readlines()
i = 0
b = 100
for i in range(7):
    if len(l[i]) < b:
        b = len(l[i])
print(b)
f2 = open('stroka.txt', "w", encoding='utf-8')
f2.writelines('Длина самой короткой строки: ')
f2.write(str(b))
