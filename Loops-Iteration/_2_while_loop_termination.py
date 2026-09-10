# Create a countdown timer that starts from a given number, prints each value down to zero, then prints "Blast off!". 
def termination(num):
    while num > 0:
        print(num)
        num -= 1
    return "Blastoff"

def main():

    num=int(input("Enter the number:"))
    result1=termination(num)
    print(result1)

main()