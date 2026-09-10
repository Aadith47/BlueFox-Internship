def convertion(num1,num2):
    intnum1=int(num1)
    intnum2=int(num2)
    return (intnum1 + intnum2)

def main():
    
    num1=input("Enter the first number ")
    num2=input("Enter the second number ")

    print(f"sum = {convertion(num1,num2)}")

main()
