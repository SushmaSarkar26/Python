class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj






# class Employee:
#  # Initializing
#  def __init__(self):
#      print('Employee created')
#  # Calling destructor
#  def __del__(self):
#      print("Destructor called")
#
#
#  def Create_obj():
#      print('Making Object...')
#      obj = Employee()
#      print('function end...')
#      return obj
#
#  print('Calling Create_obj() function...')
#  obj = Create_obj()
#  print('Program End...')





class Person:
 def __init__(self, name):
  self.name = name
  self.friend = None # Initialize the friend attribute as None
# Create two Person objects

alice = Person("Alice")
bob = Person("Bob")
# Create a circular reference by making Alice and Bob friends
alice.friend = bob
bob.friend = alice

print(alice.friend)
print(bob.friend)


