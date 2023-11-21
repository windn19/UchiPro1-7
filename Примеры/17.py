class Point:
    size = 1
    color = 'black'

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


my_point = Point()
my_point.set_coordinates(3, 5)
print(my_point.__dict__)
