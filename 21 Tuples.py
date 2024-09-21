#  Tuples are Immutable ( you can not change index value)
tup = (1, 2, 76.5, 342, 1, 32, "green", True)
# tup[0] = 90  # you can not change
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34]  # error

if 342 in tup:
    print("Yes 342 is present in this tuple")


country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")


tup2 = tup[1:4]
print(tup2)


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     # using positive indexes
print(animals[-7:-2])   # using negative indexes
print(animals[4:])      # using positive indexes
print(animals[-4:])     # using negative indexes
print(animals[1:8:3])