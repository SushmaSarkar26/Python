class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()    # overriding


rec = Shape(3, 5)
print(rec.area())

c = Circle(5)
print(c.area())









# # passing three parameters
# @dispatch(int, int, int)
# def product(first, second, third):
#     result = first * second * third
#     print(result);
#
# @dispatch(float,float,float)
# def product(first,second,third):
#  result = first * second * third
#  print(result);
# #calling product method with 2 arguments
# product(2,3,2) #this will give output of 12
# product(2.2,3.4,2.3)