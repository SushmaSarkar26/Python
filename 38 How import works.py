# import pandas
# pandas.read_csv()


# import math
#
# result = math.sqrt(9)
# print(result)  # Output: 3.0




## from keyword
# from math import sqrt, pi
#
# result = sqrt(9)
# print(result)  # Output: 3.0
#
# print(pi)  # Output: 3.141592653589793




## importing everything
# from math import *
#
# result = sqrt(9)
# print(result)  # Output: 3.0
#
# print(pi)  # Output: 3.141592653589793




## The "as" keyword
# import math as m
#
# result = m.sqrt(9)
# print(result)  # Output: 3.0
#
# print(m.pi)  # Output: 3.141592653589793



# from math import pi, sqrt as s
#
# result = s(9) * pi
# print(result)



# import math as math_builtin_python
#
# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0






## The dir function
import math

print(dir(math))
print(math.nan, type(math.nan))




from sushma import welcome, sushma
# from sushma import *

welcome()
print(sushma)



import sushma as s

s.welcome()
print(s.sushma)
