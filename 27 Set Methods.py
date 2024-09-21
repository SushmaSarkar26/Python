cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul",   "Madrid"}


cities3 = cities.union(cities2)     # all elements
print(cities3)


cities.update(cities2)
print(cities)


# cities4 = cities.intersection(cities2)     # common elements
# print(cities4)
#
#
# cities.intersection_update(cities2)
# print(cities)


# cities5 = cities.symmetric_difference(cities2)        # without common elements
# print(cities5)
#
#
# cities.symmetric_difference_update(cities2)
# print(cities)


# cities3 = cities.difference(cities2)         # remove common elements from cities
# print(cities3)
#
#
# cities.difference_update(cities2)
# print(cities)


print(cities.isdisjoint(cities2))   # if both are totally different then true


print(cities.issuperset(cities2))  # if cities2  in  cities then true    cities is superset


print(cities2.issubset(cities))    # if cities2  in  cities then true    cities2 is subset


cities.add("Helsinki")
print(cities)


cities.remove("Seoul")
print(cities)


cities.discard('Delhi')   # remove
print(cities)


item = cities.pop()   # remove first element
print(cities)
print(item)   # remove element name


# del cities["Seoul"]    # error
# print(cities)


cities.clear()
print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
