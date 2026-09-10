def parsing():
    with open("textfile.txt","r") as file:
        contents = file.read()

    words = contents.split()
    count = len(words)
    return count

def main():
    count_of_words = parsing()
    print(f"{count_of_words} words")

main()
