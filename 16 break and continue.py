for i in range(1, 51, 1):
    print(i, end=" ")
    if i == 25:
        break
    else:
        print("Mississippi")

print("Thank you")


for i in [2, 3, 4, 5, 8, 0]:
    if i % 2 != 0:
        continue
    print(i)



# An empty loop
for letter in 'elephant':
    pass
print('Last Letter :', letter)
