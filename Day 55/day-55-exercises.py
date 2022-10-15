# Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        func(args[0])
    return func

# Use the decorator 👇


@logging_decorator
def hello(name):
    print(f"function name: {name}")


hello(hello.__name__)
