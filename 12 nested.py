# Nested if

num = 18

if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif 10 < num <= 20:  # elif (num > 10 and num <= 20)
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")






i = 10
if i == 10:
    # First if statement
    if i < 15:
        print("i is smaller than 15")
        # Nested - if statement
    # Will only be executed if statement above
    # it is true
        if i < 12:
            print("i is smaller than 12 too")
        else:
            print("i is greater than 15")





# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print('*', end=' ')  # this is print without newline
    print()
