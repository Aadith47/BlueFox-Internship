to_do_list = []

def to_do(choice, task1):
    if choice == "1":
        to_do_list.append(task1)
    elif choice == "2":
        to_do_list.remove(task1)

def main():
    
    while True:
        choice = input("Enter your choice:\n1.Add\n2.Remove\n3.Display\n4.Exit\n")

        if choice == "4":
            print("Exiting.....")
            break

        elif choice == "1":
            task1 = input("Enter the task: ")
            to_do(choice, task1)
            print(f"{task1} added")

        elif choice == "2":
            to_do(choice, task1)
            print(f"{task1} removed")

        elif choice == "3":
            print(to_do_list)

        else:
            print("Invalid choice, please try again.")

main()


















# to_do_list=[]

# while True:

#     choice = input("Enter your choice:\n1.Add\n2.Remove\n3.Display\n4.Exit\n")

#     if choice == "4":
#         print("Exiting.....")
#         break

#     if choice == "1":
#         task1=input("Enter the task\n")
#         to_do_list.append(task1)
#         print(f"{task1} added suscessfully")

#     elif choice == "2":
#         to_do_list.remove(task1)
#         print(f"{task1} removed suscesfuly")

#     elif choice == "3":
#         print(to_do_list)