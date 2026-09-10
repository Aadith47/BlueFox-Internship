def slicing(word, n):
    return word[n:]

def main():
    
    word = input("Enter the string: ")
    n = int(input("Till what index: "))
    result = slicing(word, n)
    print(result)

main()
