# Default arguments
def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)


name("Amy")


# Keyword Arguments
def name(fname, mname, lname):
    print(type(name))
    print("Hello,", fname, mname, lname)


name(mname="Peter", lname="Wesker", fname="Jade")


# Required arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)


# name("Peter", "Quill")  # TypeError: name() missing 1 required positional argument: 'lname'


# Variable-length arguments
def name(*name):
    print(type(name))
    print("Hello,", name[0], name[1], name[2])


name("James", "Buchanan", "Barnes")


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i

    print("Average is: ", sum / len(numbers))


average(5, 6, 7, 1)


####  tuple
def name(**name):
    print(type(name))

    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")


# return Statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname


print(name("James", "Buchanan", "Barnes"))


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # return 7
    return sum / len(numbers)


# average(5, 6, 7, 1)   # error
c = average(5, 6, 7, 1)
print(c)
