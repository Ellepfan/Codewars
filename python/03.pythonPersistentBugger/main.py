# Напишите функцию, persistence, которая принимает положительный параметр num и возвращает его мультипликативную персистентность,
# то есть количество раз, за которое вы должны перемножить цифры num , пока не дойдете до однозначной цифры.
#
# Например (Ввод -> Вывод):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)


def persistence(n):
    count = 0
    proizv = 1
    if n > 9:
        while n % 1 > 0:
            n *= 10
        n = str(int(n))
        for i in n:
            proizv *= int(i)
        count += 1
        if proizv > 9:
            count += persistence(proizv)
    return count


persistence(39), 3
persistence(4), 0
persistence(25), 2
persistence(999), 4

# код с codewars
# def persistence(n):
#     n = str(n)
#     count = 0
#     while len(n) > 1:
#         p = 1
#         for i in n:
#             p *= int(i)
#         n = str(p)
#         count += 1
#     return count
#
# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i