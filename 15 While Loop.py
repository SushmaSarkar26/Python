# i = int(input("Enter the number: "))
# print(i)
# while i <= 38:
#     i = int(input("Enter the number: "))
#     print(i)
#
# print("Done with the loop")


count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")



# Like do-while
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
