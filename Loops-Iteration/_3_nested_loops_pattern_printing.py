def print_triangle(num):

    for i in range(1,num+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print("")
        
def main():

    num = int(input("Enter the number of rows: "))
    print_triangle(num)

main()