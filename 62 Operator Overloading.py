class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)  # overloading
print(type(v1 + v2))



print(any([False, False, False, False]))
print(any([False, True, False, False]))
print(any([True, False, True, False]))


print(all([True, True, True, True]))
print(all([False, True, True, False]))
print(all([False, False, False]))




# use 'any' function on list
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1, 11):
    list1.append(4 * i)

print(any(list1))

# Index to access the list2 is from 0 to 9
for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))






# Illustration of 'all' function in python 3

# Take two lists
list1 = []
list2 = []

# All numbers in list1 are in form: 4*i-3
for i in range(1, 21):
    list1.append(4 * i - 3)

# list2 stores info of odd numbers in list1
for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)

print('See whether all numbers in list1 are odd =>')
print(all(list2))



