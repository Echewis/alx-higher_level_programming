def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz", end=" ")
        elif a % 3 == 0:
            print("Fizz", end=" ")
        elif a % 5 == 0:
            print("BUzz", end=" ")
        else:
            print("{}".format(a), end=" ")
