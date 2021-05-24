list = []


def fizzBuzz(limit):
    for i in range(1, limit):

        if i % 3 == 0 and i % 5 == 0:
            list.append(i)
            print("FIZZBUZZ")
        elif i % 3 == 0:
            list.append(i)

            print("Fizz")
        elif i % 5 == 0:
            list.append(i)
            print("BUZZ")

        else:
            list.append(i)
            print(i)


finalList = fizzBuzz(101)


# print(list)


def primeNumber(start, end):
    # num = int(input("Enter a number: "))

    # Python program to print all
    # prime number in an interval
    # number should be greater than 1

    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    print("{}{}".format(i, " -> Not Prime"))
                    break
            else:
                print("{}{}".format(i, " -> Prime"))


value = primeNumber(1, 100)
