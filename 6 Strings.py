name = "Sushma"
friend = "Keya"
print(name + friend)

apple = '''He said, 
Hi Sushma

hey I am good
"I want to eat an apple'''

print(apple)
print("Hello, " + name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])  # Throws an error


print("Lets use a for loop\n")
for character in name:
    print(character)

for c in range(len(name)):
    print(name[c])


t = len(name)
for a in range(t-1, -1, -1):
    print(name[a])


# Zip function
l = [10,39, 84]
m = [23, 57, 95]

for a, b in zip(l, m):
    print(a, b)


t = len(l)
for h in range(t):
    print(l[h], m[h])


# strin to list
n = input("Enter the value: ")
print(n)

l = n.split(" ")
print(l)


m = []
for a in range(1, 4):
    s = input("Enter the value " +str(a)+ ":-")
    m.append(s)

print(m)



