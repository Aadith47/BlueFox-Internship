def count_vowels(s):
    count=0

    for char in (s):

        if char in "aeiouAEIOU":
            count+=1
    return count

def main():

    s=input("Enter the string:")
    result1=count_vowels(s)
    print(f"The {result1}")

main()
