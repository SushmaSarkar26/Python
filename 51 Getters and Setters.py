# Encapsulation

class MyClass:
    def __init__(self, value):
        self.__value = value

    def show(self):
        print(f"Value is {self.__value}")

    @property   # getter
    def ten_value(self):
        return 10 * self.__value

    @ten_value.setter
    def ten_value(self, new_value):
        self.__value = new_value / 10


obj = MyClass(10)
# print(obj.__value)  ## you can not access the value
print(obj.ten_value)
obj.show()

obj.ten_value = 67
print(obj.ten_value)
obj.show()
print(obj._MyClass__value)  # can be access indirectly

