def contacts():

    phonebook = {}

    while True:
            choice = input("1.Add\n2.Search\n3.Delete\n4.Display\n5.Exit\n")

            if choice == "5":
                print("Exiting.....")
                break

            if choice =="1":

                phone_num = int(input("Enter the phone number: "))
                name = input("Enter the contact name: 2")
                phonebook[name] = phone_num

            elif choice == "2":
                search_element1=input("Enter the name: ")
                if search_element1 in phonebook:
                    print(f"{search_element1} {phonebook[search_element1]}")
                else:
                    print("contact doesnt exist")

            elif choice == "3":
                search_element2 = input("Enter the contact name: ")
                if search_element2 in phonebook:
                    del phonebook[search_element2]
                    print(f"{search_element2} was deleted")
                else:
                    print(f"{search_element2} doesnt exist")

            elif choice == "4":
                print(phonebook)


def main():
    
    contacts()

main()
                
