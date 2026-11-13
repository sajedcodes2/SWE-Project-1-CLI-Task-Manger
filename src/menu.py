import quiz_data


def show_menu():
    while True:
        print("Menu:\n")
        print("1. Start Quiz\n")
        print("2. View High Scores\n ")
        print("3. Exit\n")

        choice = input("Choose an option - (Enter 1-3): ").strip()
        print(f"You chose: {choice} \n")
        if choice == "1":
            print("Let The Quiz Begin !!! \n")
            quiz_data.start_quiz()
        elif choice == "2":
            print("Let's take a look at these high scores \n")
            quiz_data.check_high_scores()
        elif choice == "3":
            print()
            break
        else:
            print("Invalid choice. Please try again.")
