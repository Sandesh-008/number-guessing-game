import random

def play_game():
    print("***** Welcome To Number Guessing Game *****")
    print("Select the level of game you want to play")
    print("\n1. Easy Level (1 - 10)\n2. Medium Level (1 - 100)\n3. Hard Level (1 - 1000)")

    try:
        ch = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input. Defaulting to Easy Level.")
        ch = 1

    if ch == 1:
        generated_num = random.randint(1, 10)
        print("Easy Level Selected (1 to 10)")
    elif ch == 2:
        generated_num = random.randint(1, 100)
        print("Medium Level Selected (1 to 100)")
    elif ch == 3:
        generated_num = random.randint(1, 1000)
        print("Hard Level Selected (1 to 1000)")
    else:
        generated_num = random.randint(1, 10)
        print("Invalid choice. Defaulting to Easy Level (1 to 10)")

    attempts = 0

    while True:
        try:
            guessed_num = int(input("\nEnter your guess: "))
            attempts += 1

            if guessed_num < generated_num:
                print("Guessed Number is too Small,Please Try Again!")
            elif guessed_num > generated_num:
                print("Guessed Number is too Large,Please Try Again!")
            else:
                print(f"Congratulations You Won the Game! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye")
            break

if __name__ == "__main__":
    main()