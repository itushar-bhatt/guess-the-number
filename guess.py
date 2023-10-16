import random

def guess_the_number():
    print("Welcome to the game")
    random_number = random.randint(0, 100)
    # print(random_number)
    guess = 0
    max_guess = 10
    guesses = 0

    while guesses < max_guess:
        try:
            guess = int(input("guess the number: "))

        except ValueError:
            print("Try a valid number")
            continue

        guesses += 1

        if guess > random_number:
            print("Too High, try again")
        elif guess < random_number:
            print("Too Low, try again")
        else:
            print(f"Congratulations!, You guessed it right in {guesses} attempts... it is {random_number}")
            break

    # else:
    print(f"Sorry, You reached a maximum guesses. The correct number is {random_number}")

    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for Playing")

guess_the_number()

# created by rohit bhatt!