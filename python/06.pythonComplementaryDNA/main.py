# Дезоксирибонуклеиновая кислота (ДНК) - это химическое вещество,
# содержащееся в ядре клетки и несущее "инструкции" по развитию и функционированию
# живых организмов.
#
# Если вы хотите узнать больше: http://en.wikipedia.org/wiki/DNA
#
# В строках ДНК символы "A" и "T" дополняют друг друга, как "C" и "G"
# Ваша функция получает одну сторону ДНК (строку, за исключением Haskell); вам
# нужно вернуть другую дополнительную сторону. Цепочка ДНК никогда не бывает пустой
# или ДНК вообще нет (опять же, за исключением Haskell).
#
# Другие похожие упражнения можно найти здесь: http://(rosalind.info/problems/list-view/
#                                                      (источник))
# Пример: (ввод --> вывод)
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    my_str = ""
    for i in dna:
        if i == "A":
            my_str += "T"
        elif i == "T":
            my_str += "A"
        elif i == "C":
            my_str += "G"
        elif i == "G":
            my_str += "C"
    return my_str


print(DNA_strand("AAAA"), "TTTT", "String AAAA is")
print(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
print(DNA_strand("GTAT"), "CATA", "String GTAT is")

# код с codewars
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])
#
#
# def DNA_strand(dna):
#     reference = { "A":"T",
#                   "T":"A",
#                   "C":"G",
#                   "G":"C"
#                   }
#     return "".join([reference[x] for x in dna])
