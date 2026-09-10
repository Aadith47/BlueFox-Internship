def string_sanitization(string):
    return string.replace(" ","_")

def main():

    string=input("Enter the string:")
    result1=string_sanitization(string)
    print(f"{result1}")

main()
