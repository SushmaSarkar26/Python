## Writing a file
# f = open('myfile.txt', 'w')    # if file not exist then create file
# f = open('myfile.txt', 'a')    # you can pass only one argument
# f.write('\nHello, world!')
# f.close()


## 'with' statement
with open('myfile.txt', 'a') as f:
  f.write("\nHey I am inside with\n")    # you can pass only one argument

  lines = ['line 1\n', 'line 2\n', 'line 3\n']  # you can pass multiple argument
  f.writelines(lines)



# Reading File

f = open('myfile.txt', 'r')   # default r mode
text = f.read()
print(text)
# print(f.read(3))
f.close()
