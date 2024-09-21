#list
l = []
for a in range(1,21):
    if a % 2 == 0:
        l.append(a)

print(l)


n = [h for h in range(1, 21) if h % 2 == 0]   #list comprehension
print(n)


s = "hello"
d = [g for g in s]
print(d)





#dict

dict = {}
for i in range(1, 10):
    if i%2 == 0:
        dict[i] = i * i

print(dict)


d = {i: i * i for i in range(1, 10) if i%2 == 0 }
print(d)





#set
l = [1, 2, 3, 2, 4, 5, 3, 6]
s = set(l)
print(s)

e = {i for i in s if i%2 == 0}
print(e)




