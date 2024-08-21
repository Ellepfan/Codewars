# Реализовать функцию, которая складывает два числа вместе и возвращает
# их сумму в двоичном формате. Преобразование может быть выполнено до или после сложения.
#
# Возвращаемое двоичное число должно быть строкой.
#
# Примеры:(Ввод1, Ввод2 --> Вывод (объяснение)))
#
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a, b):
    return format(a + b, 'b')
    # return bin(a + b)


print(add_binary(1, 1), "10")
print(add_binary(0, 1), "1")
print(add_binary(1, 0), "1")
print(add_binary(2, 2), "100")
print(add_binary(51, 12), "111111")

# код с codewars
# def add_binary(a,b):
#     return bin(a+b)[2:]
# def add_binary(a,b):
#     return '{0:b}'.format(a + b)