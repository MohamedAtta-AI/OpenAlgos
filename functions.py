def generate_fibonacci(n):
    """
    Print the first N numbers of the Fibonacci sequence

    ### Parameters:
    - n (int): The number of Fibonacci numbers to generate.

    ### Example:
    >>> generate_fibonacci(5)
    0 1 1 2 3

    ### Author:
    Mohamed Atta
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("N must be positive")

    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


def check_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def reverse_string(txt):
    return txt[::-1]


def count_vowels(input_string):

    '''
    Author:
    Mostafa Samer Dorrah
    '''
    input_string.lower()
    
    vowels = "aeiou" 
    count = 0
    
    for i in input_string:
        if i in vowels:
            count += 1
            
    return count

def calculate_average(nums):
    return sum(nums) / len(nums)


def abc():
    pass