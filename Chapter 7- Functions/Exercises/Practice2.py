# Using recursion
def factorial(n):
    """
    Calculates the factorial of a positive integer using recursion.

    Parameters:
    - n (int): The positive integer for which to calculate the factorial.

    Returns:
    - int: The factorial of the input integer.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
