numbers_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
print("Elements of the list:")
while i < len(numbers_list):
    print(numbers_list[i])
    i += 1
numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 64,81, 100)

x = int(input("Enter number to search: "))
i = 0
found = False

while i < len(numbers_tuple):
    if numbers_tuple[i] == x:
        found = True
        break
    i += 1

if found:
    print(f"{x} is present in the tuple.")
else:
    print(f"{x} is not present in the tuple.")