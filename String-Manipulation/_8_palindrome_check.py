def palindrome(string):
    reversed_string1=string[::-1]
    string.lower()
    reversed_string1.lower()

    if  string == reversed_string1:
        return "Palindrome"

    else:
        return "Not palindrome"

def main():

    string=input("Enter the string:")
    result1=palindrome(string)
    print(f"{result1}")

main()
