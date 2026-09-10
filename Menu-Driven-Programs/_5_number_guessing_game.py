import random

def play_game():

    ai_guess = random.randint(1, 5)
    count = 0

    while True:
        user_guess = int(input("Enter a number: "))
        count += 1

        if user_guess > ai_guess:
            print("The guess was higher")

        elif user_guess < ai_guess:
            print("The number was lower")
            
        else:
            print(f"Hurray!!!! The guess was right, it took {count} guesses")
            break

    return count

def main():

    high_score = None

    while True:
        choice = input("1.Play Game.\n2.View High Score.\n3.Exit.\nEnter the Choice\n")

        if choice == "3":
            print("Exiting....")
            break

        elif choice == "1":

            count = play_game()
            if high_score is None or count < high_score:
                high_score = count
                print("New high score!")

        elif choice == "2":

            if high_score is None:
                print("No games played yet")
            else:
                print(f"High score (least guess): {high_score}")

        else:
            print("Please enter a valid choice")

main()



