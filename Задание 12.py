'''
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 125 идущих подряд цифр 8?
В ответе запишите полученную строку.

НАЧАЛО
ПОКА нашлось (333) ИЛИ нашлось (888)
    ЕСЛИ нашлось (333)
        ТО заменить (333, 8)
        ИНАЧЕ заменить (888, 3)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Ответ: 388
'''

s = '8' * 125
while '333' in s or '888' in s:
    if '333' in s:
        s = s.replace('333', '8', 1)
    else:
        s = s.replace('888', '3', 1)
print(s)
