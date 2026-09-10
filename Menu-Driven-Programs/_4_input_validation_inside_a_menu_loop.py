def sum_of_two(var1, var2):
    return var1 + var2

def mul_of_two(var1, var2):
    return var1 * var2

def div_of_two(var1, var2):
    return var1 / var2

def sub_of_two(var1, var2):
    return var1 - var2

def main():
    
    while True:
        choice = input("Enter choice \n1.Addition\n2.Multiplication\n3.Division\n4.Subtraction\n5.Exit\n")

        if choice == "5":
            print("Exiting.....")
            break

        elif choice == "1":
            var1 = int(input("Enter the first number: "))
            var2 = int(input("Enter the second number: "))
            result1 = sum_of_two(var1, var2)
            print(f"{var1} + {var2} = {result1}")

        elif choice == "2":
            var1 = int(input("Enter the first number: "))
            var2 = int(input("Enter the second number: "))
            result2 = mul_of_two(var1, var2)
            print(f"{var1} * {var2} = {result2}")

        elif choice == "3":
            var1 = int(input("Enter the first number: "))
            var2 = int(input("Enter the second number: "))
            result3 = div_of_two(var1, var2)
            print(f"{var1} / {var2} = {result3}")

        elif choice == "4":
            var1 = int(input("Enter the first number: "))
            var2 = int(input("Enter the second number: "))
            result4 = sub_of_two(var1, var2)
            print(f"{var1} - {var2} = {result4}")

        else:
            print("Invalid choice, please try again.")

main()