def file_write():
    file = open("textfile.txt","w")
    file.write("Good ")
    file.write("morning ")
    file.write("everyone")
    file.close()

def file_read():
    file = open("textfile.txt","r")
    items = file.read()
    file.close()
    return items

def main():
    contents = file_read()
    print(f"The contents in the file: {contents}")

main()