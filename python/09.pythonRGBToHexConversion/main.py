# Функция rgb является неполной. Завершите ее так, чтобы передача
# десятичных значений RGB привела к возвращению шестнадцатеричного представления.
# Допустимые десятичные значения для RGB - 0 - 255.
# Любые значения, выходящие за этот диапазон, должны быть округлены до ближайшего
# допустимого значения.
#
# Примечание: Ваш ответ всегда должен состоять из 6 символов,
# сокращение с 3 здесь не сработает.
#
# Примеры (ввод --> вывод):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    my_str = ""
    my_list = [r, g, b]
    for i in my_list:
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        number_hex = str('{0:x}'.format(i)).upper()
        if len(number_hex) == 1:
            my_str = my_str + '0' + number_hex
        else:
            my_str = my_str + number_hex
    if len(my_str) in [6, 6]:
        return my_str


print(rgb(290, 246, 15))
print(rgb(0, 0, 0), "000000", "testing zero values")
print(rgb(1, 2, 3), "010203", "testing near zero values")
print(rgb(255, 255, 255), "FFFFFF", "testing max values")
print(rgb(254, 253, 252), "FEFDFC", "testing near max values")
print(rgb(-20, 275, 125), "00FF7D", "testing out of range values")

#
# код с kodewars
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))
#
#
# # def limit(num):
# #     if num < 0:
# #         return 0
# #     if num > 255:
# #         return 255
# #     return num
# #
# #
# # def rgb(r, g, b):
# #     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
