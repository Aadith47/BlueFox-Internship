def calculate_tax(income):

    if income <= 10000:
        tax = 0

    elif income <= 20000:
        tax = (income - 10000) * 0.10

    else:
        tax = 10000 * 0.10 + (income - 20000) * 0.20

    return tax

def main():
    
    income = float(input("Enter income: "))
    tax = calculate_tax(income)
    print(f"Income tax: {tax}")

main()