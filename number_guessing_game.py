import random
import time

def range_of_numbers():
    return random.randint(1, 100)

def difficulty():
    time.sleep(2)
    print("""
    Please select the difficulty level:\n
    1. Easy (10 chances)\n
    2. Medium (5 chances)\n
    3. Hard (3 chances)
    """)
    while True:
        time.sleep(2)
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            return 10, 'Easy'
        elif choice == '2':
            return 5, 'Medium'
        elif choice == '3':
            return 3, 'Hard'
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def main():
    high_scores = {'Easy': float('inf'), 'Medium': float('inf'), 'Hard': float('inf')}
    user_name = input("Enter your name: ")

    while True:
        chances, level = difficulty()
        number_to_guess = range_of_numbers()
        trials = 0
        start_time = time.time()

        time.sleep(2)
        print(f"""
Great! You have selected the {level} level with {chances} chances.
Let's start the game!
          """)

        while trials < chances:
            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                print("Please, enter a valid number.")
                continue

            trials += 1

            if guess < number_to_guess:
                print("Incorrect! You guessed below the number. Guess again:\n")
            elif guess > number_to_guess:
                print("Incorrect! You guessed above the number. Guess again:\n")
            else:
                print("Correct! You guessed the right number.")
                break

        end_time = time.time() 
        total_time = round(end_time - start_time, 2) 

        if guess == number_to_guess:
            print(f"\nWell done, {user_name}! You guessed the number in {trials} attempts and {total_time} seconds.")
            if trials < high_scores[level]:
                high_scores[level] = trials
                print(f"New high score for {level} difficulty: {trials} guesses!\n")

        else:
            print(f"Sorry, you've run out of chances. The correct number was {number_to_guess}.")
        
        print(f"High scores: {high_scores}\n")
        print(f"Time used: {total_time} seconds\n")

        play_again = input("Do you want to play another round? (yes/no): \n").strip().lower()
        if play_again != 'yes':
            break

    print(f"Thank you for playing, {user_name}!")

if __name__ == "__main__":
    main()