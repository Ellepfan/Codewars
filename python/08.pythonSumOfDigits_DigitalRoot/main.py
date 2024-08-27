# Цифровой корень - это рекурсивная сумма всех цифр в числе.
#
# Учитывая n, возьмем сумму цифр из n. Если это значение содержит более одной цифры,
# продолжайте уменьшать таким образом, пока не будет получено однозначное число. Входным числом будет неотрицательное целое число.
#
# Примеры
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    number = 0
    result = n
    while n > 9:
        for i in range(len(str(n))):
            number += n % 10
            n //= 10
        if number > 9:
            return digital_root(number)
        result = number
    return result


print(digital_root(8))
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))

# код с codewars
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
#
# def digital_root(n):
# 	return n%9 or n and 9
#
# def digital_root(n):
#     return 1 + ((int(n) - 1) % 9) if n>0 else 0