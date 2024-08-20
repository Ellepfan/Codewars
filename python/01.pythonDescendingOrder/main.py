# Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве аргумента и
# возвратить его цифрами в порядке убывания. По сути, переставьте цифры, чтобы получить максимально возможное число.
# Примеры:
# Вход: 42145 Выход: 54421
# Ввод: 145263 Вывод: 654321
# Ввод: 123456789 Вывод: 987654321

def descending_order(num):
    if isinstance(num, int) and num > 0:
        num = sorted(str(num))[::-1]
        num = ''.join(num)
        num = int(num)
    elif num == 0:
        num = 0
    return (num)


descending_order(0), 0
descending_order(15), 51
descending_order(123456789), 987654321

# решение с codewars
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))

# def Descending_Order(num):
#     return int(''.join(sorted(str(num))[::-1]))