# Полный метод/функция так, что он преобразует тире/подчеркнуть запятыми
# слова в верблюжий корпус. Первое слово в окне вывода должно быть с большой буквы
# Только если исходное слово было написано с заглавной буквы (известной как
# верхний регистр Camel, также часто называемый регистром Pascal).
# Следующие слова всегда должны быть написаны с заглавной буквы.
#
# Примеры
# "the-stealth-warrior" преобразуется в "theStealthWarrior"
# "The_Stealth_Warrior" преобразуется в "TheStealthWarrior"
# "The_Stealth-Warrior" преобразуется в "TheStealthWarrior"


def to_camel_case(text):
    my_str = ""
    i = 0
    while i < len(text):
        if text[i].isalnum():
            my_str += text[i]
            i += 1
        else:
            my_str += text[i].replace(text[i], text[i + 1].upper())
            i += 2
    return my_str


# print(to_camel_case('the_stealth_warrior'))

print(to_camel_case(""), "", "An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
      "to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
      "to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

# код с codewars
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
#
#
# def to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return words[0] + ''.join([x.title() for x in words[1:]])
#
# def to_camel_case(text):
#     return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''