def substring_search(string1,substring):
    return string1.count(substring)

def main():

    string1=input("Enter the First String: ")
    substring=input("Enter the SubString: ")
    result1=substring_search(string1,substring)
    print(f"{result1}")

main()

