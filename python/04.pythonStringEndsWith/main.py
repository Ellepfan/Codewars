# Завершите решение так, чтобы оно возвращало true, если первый переданный аргумент (строка) заканчивается вторым аргументом (также строкой).
#
# Примеры:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(text, ending):
    return text.endswith(ending)


print(solution('abc', 'bc'))  # returns true
print(solution('abc', 'd'))  # returns false
