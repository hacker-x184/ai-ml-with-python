def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
def print_numbers(n):
    if n == 0:   # Base case
        return
    print_numbers(n - 1)
    print(n)
print_numbers(5)
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print(sum_n(5))