# Starting from a positive integer, repeatedly apply: if even, divide by 2; if odd, multiply by 3 and add 1. Count the steps until the value reaches 1. 
def step_counter(num):
    count = 0

    while num != 1:

        if num % 2 == 0:
            num = num // 2

        else:
            num = num * 3 + 1
        count += 1

    print(f"Steps: {count}")

def main():

    num = int(input("Enter a starting number:"))
    step_counter(num)

main()