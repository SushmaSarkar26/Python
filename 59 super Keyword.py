class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()




class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang

keya = Employee("Keya", "420")
sushma = Programmer("Sushma", "2345", "Python")
print(sushma.name)
print(sushma.id)
print(sushma.lang)
