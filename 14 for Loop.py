name = 'Abhishek'
for i in name:
    print(i)
    if i == "b":
        print("This is something special!")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for j in color:
        print(j)

for m in range(5):
    print(m + 1)

for n in range(1, 21):
    print(n)
    # print(-n)

for k in range(1, 12, 3):
    print(k)

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

# Iterating by index
# combining else with for
list1 = ["EE", "UIT", "BU"]
print(type(list1))
for index in range(len(list1)):
    print(list1[index])
else:
    print("Inside Else Block")
