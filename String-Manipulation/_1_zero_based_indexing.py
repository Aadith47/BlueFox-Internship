def even_index(word):

    result = word[0::2]
    print(result)

def main():

    word = input("Enter a string: ")
    even_index(word)

main()