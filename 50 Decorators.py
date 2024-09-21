def greet(fx):
    def mfx(*args, **kwargs):   # arguments (tupple, dictionary)
        print("Good Morning")
        # fx()
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)


