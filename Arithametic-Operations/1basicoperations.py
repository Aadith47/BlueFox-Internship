
def sum_of_two(var1, var2):
    return var1 + var2
def mul_of_two(var1, var2):
    return var1 * var2
def diff_of_two(var1, var2):
    return var1 - var2
def quotient_of_two(var1, var2):
    return var1 / var2
def remainder_of_two(var1, var2):
    return var1 % var2
def floor_of_two(var1, var2):
    return var1 // var2

def main():

    var1=int(input("Enter the first number:"))
    var2=int(input("Enter the second number:"))

    print(f"The sum of {var1} + {var2} = {sum_of_two(var1, var2)}")
    print(f"The product of {var1} * {var2} = {mul_of_two(var1, var2)}")
    print(f"The difference of {var1} - {var2} = {diff_of_two(var1, var2)}")
    print(f"The division of {var1} / {var2} = {quotient_of_two(var1, var2)}")
    print(f"The modulus of {var1} % {var2} = {remainder_of_two(var1, var2)}")
    print(f"The floor  of {var1} // {var2} = {floor_of_two(var1, var2)}")

main()
