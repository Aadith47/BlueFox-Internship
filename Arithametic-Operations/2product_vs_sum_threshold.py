def product_of_two(var1,var2):
        return var1 * var2

def sum_of_two(var1,var2):
        return var1 + var2

def main():

        var1=int(input("Enter the first number:"))
        var2=int(input("Enter the second number:"))

        if product_of_two(var1,var2) <= 1000:
                
                print(f"{product_of_two(var1,var2)}")

        else :
                print(f"{sum_of_two(var1,var2)}")

main()
