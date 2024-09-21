x = 10  # global variable


def my_function():
    global x
    x = 8  # this will change the value of the global variable x
    print(x)
    y = 5  # local variable
    print("local variable ", y)


print("before change of global X value ", x)

my_function()
print(f"global variable {x}")  # print 8
# print(y)  # this will cause an error because y is a local variable and is not accessible outside of the function

print("After change of global X value ", x)
