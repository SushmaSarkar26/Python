letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and \n I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


# without f-strings
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))


# with f-strings
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())


print(f"{2 * 30}")
print(type(f"{2 * 30}"))
