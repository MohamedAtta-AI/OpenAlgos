def generate_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("N must be positive")

    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


N = eval(input("Enter the value of N: "))
generate_fibonacci(N)