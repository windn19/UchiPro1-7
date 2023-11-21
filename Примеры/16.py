class Point:
    size = 1
    color = 'black'

    def set_coordinates(self):
        print('Вызов метода set_coordinates')


my_point = Point()
my_point.set_coordinates()
# тоже самое что и
# Point.set_coordinates(my_point)
