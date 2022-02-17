import matplotlib.pyplot as plt
from cachetools import cached, TTLCache
import math

cache = TTLCache(maxsize=100, ttl=86400)


def main():
    print("That is a program to try to compare the results of approximation using Taylor's series and library math.")
    print("The function that is examined is sin(2x) ^ 3")
    print("With following instructions you will be able to do approximation")
    input("Print anything to continue: ")
    members = inputer("Type the amount of terms in Taylor Series: ", int)
    degrees_true = inputer("Type R if you want to input radians, type D if you want to degrees: ", bool, ["D", "d"],
                           ["R", "r"])
    value = inputer("Type the value of the x: ", float)
    if degrees_true:
        value = (math.pi * value) / 180
    value = get_into_radius_pi(value)
    result = calculation(value, members)
    close_member = search_for_close(get_into_radius_pi(value))
    print(f"The result of your inputs is {result}")
    print(f"The result of math sin is {math_pi(value)}")
    print(f"The first term, that differs from math only for 10 ^ (-6) is {close_member}")
    if inputer("If you want to create the visualisation of approximation, enter Y, otherwise enter N to Exit: ", str,
               ["Y", "y"], ["N", "n"]):
        scope = inputer(
            "Enter the scope (the value of y, that will be maximum on graph) from the actual value of the function\n"
            "Don't enter too little or too big value, if you want default value of scope just don't enter anything\n"
            "Different scopes may be useful, if you want to see how far little terms may go\n"
            "Your scope: ", float, "")
        visualise_difference(value, scope)


def calculation(radian, members):
    radian *= 2
    result = 0
    for iteration in range(members):
        result += ((-1) ** iteration * radian ** (2 * iteration + 1)) / factorial(2 * iteration + 1)
    return result ** 3


@cached(cache)
def factorial(attempt, result=1):
    """
    Returns factorial recursively
    @param attempt:
    @return:
    >>> factorial(6)
    720
    """
    if attempt == 1:
        return 1
    result *= attempt
    if attempt == 2:
        return result
    return factorial(attempt - 1, result)


def get_into_radius_pi(value):
    while value <= - math.pi / 2:
        value += math.pi
    while value >= math.pi / 2:
        value -= math.pi
    return value


def search_for_close(radian):
    math_value = (math.sin(2 * radian) ** 3)
    radian *= 2
    result = 0
    iteration = 0
    while True:
        result += ((-1) ** iteration * radian ** (2 * iteration + 1)) / factorial(2 * iteration + 1)
        if abs(result ** 3 - math_value) <= 10 ** (-6):
            return iteration
        iteration += 1


def math_pi(value):
    return math.sin(2 * value) ** 3


def visualise_difference(value, scope):
    x = []
    result = []
    x_count = 10
    for elem in range(x_count):
        x.append(elem)
        result.append(calculation(value, elem))
    x, result = x[1:], result[1:]
    minimal, maximal = min(result), max(result)

    plt.plot(x, result, color='green', linestyle='dashed', linewidth=2,
             marker='o', markerfacecolor='blue', markersize=12)

    plt.plot(x, [math_pi(value)] * len(x), linewidth=3)
    plt.plot(x, [0] * len(x), linewidth=1, color='black')

    if scope is True:
        difference = maximal - minimal
        plt.ylim(minimal - difference * 0.1, maximal + difference * 0.1)

    else:
        plt.ylim(-scope, scope)
    plt.xlim(1, x_count)

    plt.xlabel('X axis')
    plt.ylabel('The value of ')

    plt.title('Visualisation of approximation')

    plt.show()


def inputer(text, required_type, first=[], second=[]):
    while True:
        value = input(text)
        if value in first:
            return True
        if required_type == float:
            try:
                return float(value)
            except ValueError:
                print("The input is not acceptable, please, insert acceptable float value")
        elif required_type == int:
            try:
                return int(value)
            except ValueError:
                print("The input is not acceptable, please, insert acceptable integer value")
        if value in second:
            return False
        else:
            print("The input is not correct!")


if __name__ == '__main__':
    main()
