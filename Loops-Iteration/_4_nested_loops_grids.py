def multiplication_table(num):

    for i in range(1, num+1):
        for j in range(1, 11):
            print(f"{i * j}",end=" ")
        print("\n")

def main():

    num=int(input("Enter the row:"))
    multiplication_table(num)

main()
