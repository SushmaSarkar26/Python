class Person:
    name = "Sushma"
    occupation = "Software Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

print(Person)
a = Person()
b = Person()
c = Person()
d = Person()


a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Keya"
b.occupation = "HR"


print(a.name, a.occupation)
a.info()
b.info()
c.info()
print(d.name)

# del a.name    # delete
# print(a.name)
