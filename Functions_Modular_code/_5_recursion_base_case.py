def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def main():
    while True:
        try:
            num = int(input("Enter the number: "))
            factorial_result = factorial(num)
            print(f"The factorial of {num} is {factorial_result}")
        except ValueError:
            print("Please enter a valid input")

main()

