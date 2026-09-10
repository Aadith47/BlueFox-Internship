count = 0
def search(search_element):
    with open("textfile.txt", "r") as file:
        contents = file.read()

    words = contents.split()
    count = 0

    for word in words:
        if word == search_element:
            count += 1
    return count

def main():
    search_element = input("Enter the word to searched: ")
    repeatation = search(search_element)

    if repeatation == 0:
        print(f"The file does not contain the word {search_element} ")
        
    else:
        print(f"The word {search_element} is repeating {repeatation} time")

main()