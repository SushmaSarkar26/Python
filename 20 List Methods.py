l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)


      # check one by one
# l.append(7)    # add  element end
# l.sort()      # sorting decrease to increase
# l.sort(reverse=True)   # reverse sort
# l.reverse()  # reverse list
# l.pop(3)      # remove index(3) element
# l.remove(2)     # delete the element
# l.clear()       # delete all element
# print(l.index(1))    # show first index of the element(1)
# print(l.count(1))    # count the element have how much time in list
# l.replace(11, 8)  // error

print(l)

m = l.copy()
m[0] = 0
print(m)

l.insert(1, 899)
print(l)

m = [900, 1000, 1100]
l.extend(m)

print(l)

# k = l + m
# print(k)

