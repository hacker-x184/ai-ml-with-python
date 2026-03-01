def sum(a,b):
    s= a+b
    return s
result  = sum(5,64)
print(result)
def print_length(my_list):
    print("Length of list is:", len(my_list))
numbers = [1, 2, 3, 4, 5]
print_length(numbers)
def print_elements(my_list):
    for item in my_list:
        print(item, end=" ")
numbers = [10, 20, 30, 40]
print_elements(numbers)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial is:", result)
def usd_to_inr(usd):
    rate = 83
    inr = usd * rate
    return inr
amount = float(input("Enter amount in USD: "))
print("Amount in INR:", usd_to_inr(amount))
