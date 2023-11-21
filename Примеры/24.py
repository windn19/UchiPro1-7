class Point:
    MAX_SIZE = 10

    @classmethod
    def validate_size(cls, size):
        return size <= cls.MAX_SIZE

    def set_size(self, size):
        if self.validate_size(size):
            self.size = size
        else:
            self.size = self.MAX_SIZE


print(Point.validate_size(15))  # False
my_point = Point()
my_point.set_size(15)
print(my_point.size)  # 10
