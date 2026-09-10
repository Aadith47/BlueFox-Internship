def celsius_to_fahrenheit(var1):
    return (var1 - 32) * 5/9

def fahrenheit_to_celsius(var1):
    return (var1 * 9/5) + 32

def main():
    var1 = float(input("Enter the temprature "))
    choice = input("Convert into Celcius:C Fahrenheit:F  ")

    if choice == "C":
        print(f"{celsius_to_fahrenheit(var1)}")

    elif choice == "F":
        print(f"{fahrenheit_to_celsius(var1)}")

    else:
        print("Invalid Choice")

main()
