def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error"


def multi(x, y):
    return x * y


def wrong_op():
    print("Wrong operator")


if __name__ == "__main__":
    ops = {"+": add,
           "-": sub,
           "/": div,
           "*": multi
           }

    num1 = float(input("number 1: "))
    operator = input("+, - , /, *: ")
    num2 = float(input("number 2: "))

    result = ops.get(operator, wrong_op)(num1, num2)
    print(f"{num1}{operator}{num2} = {result}")
