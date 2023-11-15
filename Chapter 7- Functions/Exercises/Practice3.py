# Prime number or not
def is_prime(number):
    """
    Checks if a given number is prime.

    Parameters:
    - number (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
    return True 

input_number = int(input("Enter a number to check for primality: "))
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")