class Person:

    def __init__(self, name, occ):   # Parameterized constructor
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Sushma", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()


print(a.name)
a = Person("Keya", "HR")
a.info()







# Use the any word like  mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()




# If you for some reason have a class definition with no content, put in the pass statement
# to avoid getting an error.

class Person:
  pass





class Person:
 #2 “_” at both sides of init
 def __init__(self, name, age):
   self.name = name
   self.age = age

 def myfunc(self):
  print("Hello my name is " + self.name)

p1 = Person("som", 46)
p1.myfunc()





