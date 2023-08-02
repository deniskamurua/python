# Function with inputs, fuctionality and output

def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


# Function as arguments

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


results = calculate(add, 3, 5)
print(results)


# Function nested in other functions

def outer_function():
    print("outter function")

    def inner_function():
        print("inner function")

    inner_function()


outer_function()


# Function can be returned from other functions

def otter_function():
    print("outter function")

    def nested_function():
        print("inner function")

    return nested_function


innerr_function = otter_function()
innerr_function()
