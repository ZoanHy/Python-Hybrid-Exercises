def add(*args):
    # type(args) --> tuple
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 5, 6, 7, 89, 1))


def calculate(n, **kwargs):
    # type **kwargs --> dict
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=10)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


# my_car = Car(make = "Toyota", model="TYT2002")
my_car = Car(make="Toyota", colour="red")

print(my_car.make, my_car.colour)
