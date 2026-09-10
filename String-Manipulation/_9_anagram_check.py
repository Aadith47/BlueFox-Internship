def anagram_checker(string1, string2):
    letters1=sorted(string1.lower())
    letters2=sorted(string2.lower())

    if letters1==letters2:
        return "anagram"
    
    else:
        return "Not anagram"

def main():

    string1=input("Enter the first string:")
    string2=input("Enter the second string:") 
    result1=anagram_checker(string1, string2)
    print(result1)

main()