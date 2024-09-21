ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)    # delete
# ep1.popitem()   # delete last item
# del ep1  # throw error
# del ep1[122]

print(ep1)

print(ep1.setdefault(123))
print(ep1[123])

info = {'name': 'Sushma', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2004})
print(info)




cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]
z = zip(cities, countries)
print(type(z))

# for a in z:
#     print(a, end=' ')

dict = {cities: countries for cities, countries in z}

print(dict)



