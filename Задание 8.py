'''
Борис составляет 6-буквенные коды из букв Б, О, Р, И, С.
Буквы Б и Р нужно обязательно использовать ровно по одному разу,
букву С можно использовать один раз или не использовать совсем,
буквы О и И можно использовать произвольное количество раз или не использовать совсем.
Сколько различных кодов может составить Борис?
Ответ: 1440
'''

import itertools

listString = itertools.product('БОРИС', repeat=6)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)