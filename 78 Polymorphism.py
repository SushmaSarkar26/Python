# polymorphism is Overriding and Overloading


# def add(x, y, z=0):
#     return x + y + z
#
#
# # Driver code
# print(add(2, 3))
# print(add(2, 3, 4))







# def my_function(*args):
#     if len(args) == 1:  # Code for one argument
#         result = args[0]
#     elif len(args) == 2:  # Code for two arguments
#         result = args[0] + args[1]
#     else:
#         raise TypeError("Unsupported number of arguments")
#
#     return result
#
#
# # Call the function with one or two arguments
# print(my_function(5))
# print(my_function(5, 3))








# class India():
#
#  def capital(self):
#         print("New Delhi is the capital of India.")
#
#  def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#  def type(self):
#         print("India is a developing country.")
#
#
#
#
# class USA():
#
#  def capital(self):
#        print("Washington, D.C. is the capital of USA.")
#
#  def language(self):
#        print("English is the primary language of USA.")
#
#  def type(self):
#        print("USA is a developed country.")
#
#
#  # obj_ind = India()
#  # obj_usa = USA()
#  # for country in (obj_ind, obj_usa):
#  #  country.capital()
#  #  country.language()
#  #  country.type()
#
#
#
# # alternate apporach
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)












class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
