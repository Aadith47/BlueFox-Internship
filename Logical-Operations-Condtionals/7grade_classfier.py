def main():

    grade=int(input("Enter the score:"))

    if grade > 89:
        print("A")

    elif grade > 79:
        print("B")

    elif grade > 69:
        print("C")

    elif grade > 59:
        print("D")

    elif grade > 49:
        print("E")

    else:
        print("F")
        
main()