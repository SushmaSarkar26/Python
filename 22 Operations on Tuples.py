tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)

res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)  # error
# res = tuple1.index(3, 4, 8)  # Value, start, stop
# res = len(tuple1)
print(res)


# Manipulating Tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)


# add tuple
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# countries.extend(countries2)  # error
# print(countries)

