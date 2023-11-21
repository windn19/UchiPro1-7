# Напиши программу, в которой создай класс Polygon (многоугольник) без атрибутов.  Реализуй в классе следующие методы:
#     • set_vertices_count(n) — добавляет объекту атрибут — количество вершин;
#     • set_coordinates(coords) — добавляет объекту атрибут — список кортежей координат многоугольника
#     • get_side_length(k) — возвращает длину стороны k этого многоугольника с точностью до сотых.
#
# Считай с клавиатуры одно целое число n — количество вершин, затем считай n пар целых чисел x, y — координаты вершин
# многоугольника. Создай экземпляр класса, используя методы добавь объекту атрибуты
# со значениями которые ты считал с клавиатуры.
#
# Считай с клавиатуры номер стороны k и используя метод get_side_length()
# выведи длину этой стороны с точностью до сотых.
#
# Входные данные:
# Вводится одно целое число n — количество вершин.
# Затем вводятся n пар целых чисел через пробел — координаты x y.
# Вводится номер стороны k (нумерация начинается с 1).
# Выходные данные:
# Выводится длина стороны с точностью до сотых.
#
# Пример ввода:
# 5
# 1 1
# 2 2
# 4 1
# 3 0
# 2 -1
# 1
# Пример вывода:
# 1.41

class Polygon:
    def set_vertices_count(self, n):
        self.n = n

    def set_coordinates(self, coords):
        self.coords = coords

    def get_side_length(self, k):
        if k == self.n:
            length = ((self.coords[0][0] - self.coords[k - 1][0]) ** 2 +
                      (self.coords[0][1] - self.coords[k - 1][1]) ** 2) ** 0.5
        else:
            length = ((self.coords[k][0] - self.coords[k - 1][0]) ** 2 +
                      (self.coords[k][1] - self.coords[k - 1][1]) ** 2) ** 0.5
        return round(length, 2)


n = int(input())
coords = []
for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

polygon = Polygon()
polygon.set_vertices_count(n)
polygon.set_coordinates(coords)
k = int(input())
print(polygon.get_side_length(k))
