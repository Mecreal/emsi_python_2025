# factorial


n = int(input("Enter a non-negative integer: "))
def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        factorial = 1
    else:
        for i in range(2, n + 1):
            factorial = factorial * i
    return factorial


fact = calculate_factorial(n)
print(f"The factorial of {n} is {fact}.")