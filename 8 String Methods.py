# Strings are immutable
a = "  !!!Sushma!! !!!!!!!!! sushma !!!!!!    "
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.title())
print(a.swapcase())
print(a.count(' '))      # how many spaces
print(a.lstrip())   # no_space_begin_text  # remove
print(a.rstrip())   # no_space_end_text  # remove
print(a.rstrip("!"))  # IF '!' is last then delete
print(a.strip())    # both side space remove
print(a.replace("Sushma", "Keya"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

print(chr(65))
print(int('A'))

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("Sushma"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# print(str1.index("ishh"))  // error

str1 = "WelcomeToTheConsole26"
print(  # Check for Alphanumeric Characters
    str1.isalnum())  # returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations or space are present, then it returns False.

str1 = "Welcome298"
print(
    str1.isalpha())  # returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "hello world"
print(str1.islower())

text = 'THIS IS A REGULAR TEXT'
print(text.isupper())

text = 'This $ Is @ A Regular 3 Text!'
print(text.istitle())

word = '32'
print(word.isnumeric())   # only number in string  no space or chars
print("\u2083".isnumeric())  # true   # unicode for subscript 3

print(word.isdigit())  # like numeric   # only number in string  no space or chars
print("\u2083".isdigit())  # true

print(word.isdecimal())   # only decimal number in string  no space or chars
print("\u2083".isdecimal())  # false

word = 'beach'
print(word.isalpha())   # only letters in string  no space or chars

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())   # returns True only if the entire string have 'space'
text = '\f\n\r\t\v'
print(text.isprintable())

# only space no text
str1 = "         "       # using Spacebar
print(str1.isspace())
str2 = "  "  # using Tab
print(str2.isspace())
text = ' \f\n\r\t\v'
print(text.isspace())

str1 = "World Health Organization"
print(str1.istitle())  # returns True only if the first letter of each word of the string is capitalized

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))
print(str1.startswith("Interpreted", 14))
print(str1.startswith("Interpreted", 14, 33))
print(str1.startswith("Interpreted", 14, 18))
print(str1.startswith(("Python", "Interpreted"), 0, 14))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())  # Upper case are converted to lower case and lower case to upper case

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  # capitalizes first letter of the each word within the string


words = "Tokyo" * 3
print(words)


# Notice that the \s represents not only space ' ', but also form
# feed \f, line feed \n, carriage return \r, tab \t, and vertical tab \v


import re
phrase = ' Do or do not there is no try '
phrase_no_space = re.sub(r'\s+', '', phrase)    # Remove All White Spaces
print(phrase)
print(phrase_no_space)

my_words = phrase.split(" ") # my_words is a list
for word1 in my_words:
  print(word1)

print(my_words)
print(my_words[3])




# Empty String or not

my_string = ''
if not my_string:
  print("My string is empty!!!")
my_string = 'amazon, microsoft'
if my_string:
  print("My string is NOT empty!!!")



# justify


word = 'town'
number_chars = 32

# word_justified = word.rjust(number_chars)     # Right-justify
# word_justified = word.ljust(number_chars)     # Left-justify

char = '$'
word_justified = word.rjust(number_chars, char)    # Right-justify
word_justified = word.ljust(number_chars, char)    # Left-justify

print(word)
print(word_justified)


# Join Items of an Iterable

my_string = 'beach'
print('$'.join(my_string))

my_list = ['bmw', 'ferrari', 'mclaren']
print('$'.join(my_list))

my_dict = {'bmw': 'BMW I8', 'ferrari': 'Ferrari F8', 'mclaren': 'McLaren 720S'}
print(','.join(my_dict))


# Split a String at Line

my_string = 'world \n cup'
print(my_string.splitlines())
print(my_string.splitlines(True))




# Set the Number of Spaces for a Tab

my_string = 'B\tR'  # tabsize = 8  # default
print(my_string.expandtabs())

my_string = 'WORL\tD'
print(my_string.expandtabs())

my_string = 'B\tR'
print(my_string.expandtabs(4))  # tabsize is 4, which gives us 3 spaces after the char 'B'



# Center a String
word = 'beach'
word_centered = word.center(32)
word_centered = word.center(33, '$')

word_zeros = word.zfill(32 )



phrase = "This is a regular text"
print(phrase.find('This'))
print(phrase.find('regular'))
print(phrase.find('regular', 0, 17))
print(phrase.find('a', 0, 15))



# Remove a Prefix or a Suffix
'Rio de Janeiro'.removeprefix("Rio")
'Rio de Janeiro'.removesuffix("eiro")
