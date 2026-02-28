print("Even numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print("Odd numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i)
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)
rows = 5

for i in range(1, rows + 1):
    print("*" * i)