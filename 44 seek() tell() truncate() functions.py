with open('myfile.txt', 'r') as f:
  print(type(f))
  # Move to the 10th byte in the file
  f.seek(10)

  print(f.tell())

  # Read the next 5 bytes
  data = f.read(5)
  print(data)



with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)   # print first 3 letters

with open('sample.txt', 'r') as f:
  print(f.read())
