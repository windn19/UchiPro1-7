# 3. Напиши программу, в которой создай класс User с атрибутом MAX_LENGTH = 20. Реализуй в классе следующие методы:
#     • @classmethod validate_length() — проверяет, что длина имени не должна превышать значение атрибута MAX_LENGTH
#     и возвращает True или False;
#     • @staticmethod validate_name() — проверяет, что имя состоит только из букв и возвращает True или False.
# Считай с клавиатуры одну строку — имя пользователя. Выведи результат метода validate_length() и validate_name()
# для данного имени на разных строках.
#
# Входные данные:
# Вводится одна строка — имя.
# Выходные данные:
# Выводятся две строки, на каждой True или False.
#
# Пример ввода:
# user
# Пример вывода:
# True
# True

class User:
    MAX_LENGTH = 20

    @classmethod
    def validate_length(cls, name):
        return len(name) <= cls.MAX_LENGTH

    @staticmethod
    def validate_name(name):
        return name.isalpha()


name = input()
print(User.validate_length(name))
print(User.validate_name(name))
