# Число 89 89 это первое целое число, состоящее более чем из одной цифры, которое удовлетворяет свойству,
# частично представленному
# в названии этого ката. Какой смысл говорить "Эврика"?
# Потому что эта сумма дает одно и то же число: 89 = 8 1 + 9 2 89=8 1 +9 2
# Следующее число, обладающее этим свойством, является 135 135:
# Посмотрите это свойство еще раз: 135 = 1 1 + 3 2 + 5 3 135=1 1 +3 2 +5 3


# Задание Нам нужна функция для сбора этих чисел, которая может принимать два целых числа 𝑎 a, 𝑏
# b это определяет диапазон [ 𝑎 , 𝑏 ] [a,b] (включительно) и выводит список отсортированных чисел в диапазоне,
# который удовлетворяет описанному выше свойству.


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    list_sum_number = []
    for i in range(a, b + 1):
        str_number = str(i)
        sum_number = 0
        for number in range(len(str_number)):
            sum_number += (int(str_number[number]) ** (number + 1))
        if sum_number == i:
            list_sum_number.append(i)
    return list_sum_number


# print(sum_dig_pow(89, 90))

print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89), [89])
print(sum_dig_pow(10, 100), [89])
print(sum_dig_pow(89, 135), [89, 135])

# код с codewars
# def sum_dig_pow(a, b):
#     return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]