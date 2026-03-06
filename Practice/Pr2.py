num1 = int(input("Enter number 1 here:--"))
num2 = int(input("Enter number 2 here:--"))
num3 = int(input("Enter number 3 here:--"))
if ((num1>num2)&(num1>num3)):
    print("Number ",num1,"is a greatest from all")
elif((num2>num1)&(num2>num3)):
    print("Number",num2," is a greatest from all")
else:
    print("Number",num3," is a greatest from all")
