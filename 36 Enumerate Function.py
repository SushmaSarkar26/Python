marks = [12, 56, 32, 98, 16, 45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Sushma, awesome!")
#   index +=1


for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print("Sushma, awesome!")





fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)




fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')




s = 'hello'
for index, c in enumerate(s):
    print(index, c)

