class Employee(object):
  def __init__(self, name):
    self.name = name
  def sho(self):
    print(f"The name is {self.name}")

class Dancer(object):
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
# o.sho()
print(DancerEmployee.mro())