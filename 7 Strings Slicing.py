#  --->   0, 1, 2, 3 .......
#  <---   -1, -2, -3 .......

fruit = "Mango"
mangoLen = len(fruit)
print("length is:", mangoLen)
print(fruit[0:4])  # including 0 but not 4
print(fruit[1:4])
print(fruit[:5])
print(fruit[:])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-3: ])
print(fruit[-3:-1])
print(fruit[2:4])
print(fruit[-1:len(fruit) - 3])  ##
print(fruit[-3: -0])  ##

print(fruit[1:4:2])    # [start:stop:step]
print(fruit[::-1])   # reverse
print(fruit[-1::-1])   # reverse
print(fruit[::2])
print(fruit[::-2])
