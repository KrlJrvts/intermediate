
# assert - do not use in production code ever!
def hi():
    print("before")
    assert 1 == 3


# Divide by 0 error ZeroDivisionError
def zero_error():
    a = 3
    b = [1, 2, 0]
    for n in b:
        try:
            result = a/n
        except ZeroDivisionError:
            # exception if there is an ZeroDivisionError
            print("You were trying to divide with zero")
            continue
        print(result)


# hi()
zero_error()
