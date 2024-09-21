# 1) Arithmetic Operators  ( +, -, *, /, //, %, ** )
# 2) Logical / Relational  ( and, or, not ) true / false   [ c/ c++  (1/0) ]
# 3) Bitwise Operators ( &, |, ~, ^, >>, >> )
# 4) Conditional / Comparison operators ( >, <, >=, <=, ==, != )   1/0   [java  (true / false) ]
# 5) Identify operators  ( is, is not )
# 6) Assignment Operators ( =, +=, -=, *=, /=, %=, //=, ^=, >>=, <<= )
# 7) Membership Operators ( in, not in )
# 8) Ternary / Conditional operators ( [on_true] if [expression] else [on_false] )



# Arithmetic Operators
# +, -, *, /, //, %, **

print(5+6)
print(15-6)
print(15*6)
print(15/6)    # division (float)
print(15//6)   # division (integer / floor)
print(5 % 4)    # modulus
print(2**4)     # power



# Logical / Relational Operators
# and, or, not

print("Relational Operators ")
# c = 1
# d = 0
c = True
d = False
print(65>34 and 78>95)
print(c and d)
print(c or d)
print(not d)



# Bitwise Operators
# &, |, ~, ^, >>, >>

print("\nBitwise Operators")
a = 10
b = 4
# Print bitwise AND operation
print(a & b)
# Print bitwise OR operation
print(a | b)
# Print bitwise NOT operation
print(~a)
# print bitwise XOR operation
print(a ^ b)
# print bitwise right shift operation
print(a >> 2)
# print bitwise left shift operation
print(a << 2)




# Conditional / Comparison operators
# >, <, >=, <=, ==, !=

print("Comparison operators")
s = 23
print(s > 18)
print(s >= 18)
print(s < 18)
print(s <= 18)
print(s == 18)
print(s != 18)    # <>


# # Identify operators
# # is, is not    # error
#
# print(s is 18)
# print(s is not 18)




# Assignment Operators
# =, +=, -=, *=, /=, %=, //=, ^=, >>=, <<=

print("Assignment Operators")
m = 10
# Assign value
n = m
print(n)
# Add and assign value
n += m
print(n)
# Subtract and assign value
n -= m
print(n)
# multiply and assign
n *= m
print(n)
# division and assign
n /= m
print(n)
# division and assign
n //= m
print(n)
# modulus and assign
n %= m
print(n)

# # and assign
# n &= m
# print(n)
# # or assign
# n |= m
# print(n)
# # xor assign
# n ^= m
# print(n)
# # bitwise right shift operator
# n >>= m
# print(n)
# # bitwise left shift operator
# n <<= m
# print(n)





# Membership Operators
# in, not in

print("Membership Operators")
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
 print("x is NOT present in given list")
else:
 print("x is present in given list")

if (y in list):
 print("y is present in given list")
else:
 print("y is NOT present in given list")





 # Ternary / Conditional operators
 #  Syntax :   [on_true] if [expression] else [on_false]

 p, q = 10, 20
 # Copy value of p in min if p < q else copy q
 min = p if p < q else q
 print(min)



print(5/2)
print(5/2.3)
print(5.9/2)
print(5.5/2.3)


print(5//2)
print(5//2.3)
print(5.9//2)
print(5.5//2.3)


num = 17
print('Binary of number 17 is:', format(num, 'b'))

