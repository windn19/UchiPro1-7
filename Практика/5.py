# 5. Напиши программу, в которой создай класс Field (игровое поле). Поле представляет из себя таблицу шириной (width) и
# высотой (height) состоящую из чередующихся 0 и 1, в левом верхнем углу которой всегда стоит 1.
# При создании объекта класса необходимо указать ширину (width) и высоту (height) поля.
# При выводе объекта на экран должна выводиться таблица без пробелов и пустых строк.
#
# Считай с клавиатуры ширину и высоту поля, создай экземпляр класса Field с этими параметрами и выведи на экран.
#
# Входные данные:
# Вводится два целых числа — ширину и высоту поля.
#
# Выходные данные:
# Выводится текстовое представление объекта.
#
# Пример ввода:
# 5
# 3
#
# Пример вывода:
# 10101
# 01010
# 10101

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []
        counter = 1
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(str(counter))
                counter = (counter + 1) % 2
            self.field.append(temp)

    def __str__(self):
        text = ''
        for i in range(self.height):
            text += ''.join(self.field[i]) + '\n'
        return text


width, height = int(input()), int(input())
field = Field(width, height)
print(field)
