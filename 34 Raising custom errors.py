# a = int(input("Enter any value between 5 and 9: "))
#
# if a < 5 or a > 9:
#     raise ValueError("Value should be between 5 and 9")





b = input("Enter any value between 5 and 9:  ")
if b == "quit":
    print("Thank You")
else:
    b = int(b)
    if b < 5 or b > 9:
        raise ValueError("Value should be between 5 and 9")




class MyError(Exception):
 # Constructor or Initializer
 def __init__(self, value):
    self.value = value
 # __str__ is to print() the value
 def __str__(self):
     return(repr(self.value))

try:
 raise(MyError(3*2))
# Value of Exception is stored in error
except MyError as error:
 print('A New Exception occurred: ', error.value)

