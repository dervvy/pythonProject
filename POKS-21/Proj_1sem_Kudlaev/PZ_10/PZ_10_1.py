# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Количество положительных элементов в первой половине:

# создание текстового файла
a = '-30 60 7 42 -22 -8 66 89'
f1 = open('new_file_1.txt', 'w')
f1.writelines(a)
f1.close()
# создание текстового файла №2
f2 = open('new_file_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(a)
f2.write('\n')
f2.close()

f1 = open('new_file_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
c = str(len(k))
d = str(min(k))
f1.close()
# ввод информации в текстовый файл
f2 = open('new_file_2.txt', 'a', encoding='UTF-8')
f2.write('Количество элементов: ')
f2.writelines(c)
f2.write('\n')
f2.write('Минимальный элемент: ')
f2.writelines(d)
f2.write('\n')
f2.close()

f1 = open('new_file_1.txt')
a = [-30, 60, 7, 42, -22, -8, 66, 89]
p = 0
for i in range(round(len(k)/2)):
    if k[i] > 0:
        p += 1
f1.close()

f2 = open('new_file_2.txt', 'a', encoding='UTF-8')
f2.write('Количество положительных элементов в первой половине: ')
f2.writelines(str(p))
f2.close()
