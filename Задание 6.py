'''
Определите, при каком наибольшем введённом значении переменной s программа выведет число 64.
Для Вашего удобства программа представлена на четырёх языках программирования.

    s = int(input())
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    print(n)

Ответ: 259
'''


# Помещаем всю программу внутрь функции, заменив входные данные параметрами функции (s)
# Результат функции - это значение переменной, которую выводит на экран представленный алгоритм (n)
def f(s):
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    return n


# Перебираем все значения функции для нахождения необходимого нам значения
# Решением будет последнее значение, т.к. необходимо найти наибольшее значение
for i in range(10000):
    if f(i) == 64:
        print(i)
