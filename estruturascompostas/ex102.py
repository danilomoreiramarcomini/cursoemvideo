def factorial(parameter_factorial, show=False):
    """ This function calc the factorial of parameter_factorial and the show is optional to see the values of the
    calculation
    :param parameter_factorial: The value entered  user to calculation of factorial
    :param show: The optional value to see the values or not
    :return: Factorial of parameter_factorial entered
    """
    support = int(1)

    if not show:
        for number in range(parameter_factorial, 0, -1):
            support *= number

        print(support)
    if show:
        for number in range(parameter_factorial, 0, -1):
            support *= number
            print(number, end=" ")
            if number > 1:
                print("*", end=" ")
            else:
                print("=", end=" ")
        print(support)


factorial(int(input("Factorial: ")), True)
