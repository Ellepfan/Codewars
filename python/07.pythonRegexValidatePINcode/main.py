# Банкоматы допускают использование 4-или 6-значных PIN-кодов,
# а PIN-коды могут содержать только ровно 4 или 6 цифр.
#
# Если функции передана допустимая строка PIN, верните true, иначе верните false.
# Примеры (Ввод -> Вывод)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

print(validate_pin('123 '), "ответ")
print(validate_pin("123456"))
print(validate_pin("0000"))
print(validate_pin("+1111"))
print(validate_pin("-111"))
print(validate_pin("098765"))
print(validate_pin("000000"), "ответ")
print(validate_pin("12f456"), "ответ")
print(validate_pin("av0909"), "ответ")
print(validate_pin("09876"), "ответ")
print(validate_pin('123 '), "ответ")