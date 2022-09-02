import os
os.system("cls")


def prime_checker(number):
    if number < 2:
        print("It's not prime number")
    if number == 2:
        print("It's prime number")
    else:
        if number % 2 == 0:
            print("It's not prime number")
        else:
            check = False
            for num in range(4, number + 1 ):
                if number % num == 0:
                    check = True
            if not check:
                print("It's prime number")
            else:
                print("It's not prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)