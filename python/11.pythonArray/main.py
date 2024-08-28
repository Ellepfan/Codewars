# Ваша цель в этом ката - реализовать функцию разности,
# которая вычитает один список из другого и возвращает результат.
# Он должен удалить все значения из списка a, которые присутствуют в списке b сохраняя
# их порядок.
# array_diff([1,2],[1]) == [2]
# Если значение присутствует в b, все его вхождения должны быть удалены из другого:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]


# def array_diff(a, b):
#     if len(a) > 0 and len(b):
#         count_a = 0
#         while count_a < len(a):
#             count_b = 0
#             while count_b < len(b):
#                 if b[count_b] == a[count_a]:
#                     a.remove(a[count_a])
#                     count_b += 1
#                     continue
#                 else:
#                     count_a += 1
#             count_a += 1
#             print(a)
#     return a


def array_diff(a, b):
    return [A for A in a if A not in b]


print(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
print(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
print(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
print(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
print(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

# код с codewars
# def array_diff(a, b):
#     #your code here
#     return filter(lambda i: i not in b, a)
#
# def array_diff(a, b):
#     for n in b:
#         while(n in a):
#             a.remove(n)
#     return a