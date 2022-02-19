import sys
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
    radius_pi = inputer(f'Do you want to get your input into radius of pi (to have better accuracy).\n'
                        f'Otherwise, there mey occur errors.\n'
                        f'Print Y to confirm or N to decline: ', str, ["Y", "y"], ["N", "n"])
    if degrees_true:
        value = (math.pi * value) / 180
    if radius_pi:
        value = get_into_radius_pi(value)
    try:
        result = calculation(value, members)
    except OverflowError:
        print("Sorry, the numbers are too big, try to start the program with different values")
        sys.exit()
    print(f"The result of your inputs is {result}")
    print(f"The result of math sin is {math_pi(value)}")
    print(f"The first term, that differs from math only for 10 ^ (-1) is {search_for_close(value, 10 ** (-1))}\n"
          f"The first term, that differs from math only for 10 ^ (-4) is {search_for_close(value, 10 ** (-4))}\n"
          f"The first term, that differs from math only for 10 ^ (-6) is {search_for_close(value, 10 ** (-6))}")
    if inputer("If you want to create the visualisation of approximation, enter Y, otherwise enter N to Exit: ", str,
               ["Y", "y"], ["N", "n"]):
        scope = inputer(
            "Enter the scope (the value of y, that will be maximum on graph) from the actual value of the function\n"
            "Don't enter too little or too big value, if you want default value of scope just don't enter anything\n"
            "Different scopes may be useful, if you want to see how far little terms may go\n"
            "Your scope: ", float, "")
        terms = inputer(f"How many terms do you want to show: ", int)
        visualise_difference(value, scope, terms)

@cached(cache)
def calculation(radian, members):
    result = 0
    for iteration in range(members + 1)[1:]:
        result += (-1) ** iteration * 2 ** (2 * iteration + 1) * (-1 + 9 ** iteration)\
        * radian ** (2 * iteration + 1) / factorial(2 * iteration + 1)
    return result * (-3 / 4)

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
    return value % (math.pi * 2)


def search_for_close(radian, range):
    iteration = 0
    try:
        while True:
            if abs(calculation(radian, iteration) - math_pi(radian)) <= range:
                return iteration
            iteration += 1
    except:
        return "impossible to reach"


def math_pi(value):
    return math.sin(2 * value) ** 3


def visualise_difference(value, scope, x_count):
    x = []
    result = []
    for elem in range(x_count):
        x.append(elem)
        result.append(calculation(value, elem))
    x, result = x[1:], result[1:]
    minimal, maximal = min(result), max(result)

    plt.plot(x, result, color='green', linestyle='dashed', linewidth=2,
             marker='o', markerfacecolor='blue', markersize=11)

    plt.plot(x, [math_pi(value)] * len(x), linewidth=3, color="red")
    plt.plot(x, [0] * len(x), linewidth=1, color='black')

    if maximal == minimal:
        scope = 0.5
    if scope is True:
        difference = maximal - minimal
        plt.ylim(minimal - difference * 0.1, maximal + difference * 0.1)

    else:
        plt.ylim(-scope, scope)
    plt.xlim(1, x_count)

    plt.xlabel('Terms')
    plt.ylabel('The value of Approximation')

    plt.title(f'Visualisation of Approximation for x = {value}')

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
