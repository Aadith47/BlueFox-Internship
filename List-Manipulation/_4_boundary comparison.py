def palindrome(list1):

    list2=list1[::-1]

    if list1[0] == list2[0]:
        print("true")

    else:
        print("False")


def main():

    list1=input("Enter the string: ")

    palindrome(list1)

main()

