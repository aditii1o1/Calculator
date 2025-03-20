num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Please Enter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division\n")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

