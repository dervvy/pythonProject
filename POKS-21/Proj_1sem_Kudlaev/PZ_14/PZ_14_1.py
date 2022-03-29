# Из исходного текстового файла (Dostoevsky.txt) выбрать блок
# информации за 1857 год и поместить ее в новый текстовый файл.

import re
p = re.compile(r'1857')
with open('Dostoevsky.txt', encoding='utf-8') as f: # открытие файла
    a = f.read()
    b = re.findall(p, a) # поиск по файлу
with open('1857.txt', 'w', encoding='utf-8') as f2: # создание нового файла
    f2.write(str(b[0]))

h = re.compile(r'\n')

with open('Dostoevsky.txt', encoding='utf-8') as f:
    t = f.read()
    l = re.split(h, t)

c = l.index('1857 год')
d = l.index('1860–1866 гг.')
with open('1857.txt', 'a', encoding='utf-8') as f2:
        for i in l: # поиск границ блока
            if i == '1857 год':
                for v in l[c+1:d]:
                    if v != '1860–1866 гг.':
                            f2.write(f'\n{v}')
