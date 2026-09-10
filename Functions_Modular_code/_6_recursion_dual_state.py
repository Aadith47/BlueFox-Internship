def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    while True:
        try:
            num=int(input("Enter the number: "))
            fibonacci_number=fibonacci(num)
            print(f"The nth fibonacci number of {num} is {fibonacci_number}")
        except ValueError:
            print("Please type a valid input")
            
main()