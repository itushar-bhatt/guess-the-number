# old_age = input("what is your 2 years old age?")
# new_age = int(old_age) + 2 
# print("the new age is " + str(new_age))

# first_number = input("Enter first number :")
# second_number = input("Enter second number :")

# sum = int(first_number) + int(second_number)
# print("The sum is :" " " + str(sum))

# name = input("what is Your good name?")
# age = input("What is your age?")
# print("Hello" + " " + name)

# name = "Rohit Bhatt"
# print(name.upper())
# print(name.lower())
# print(name.find('t'))

# name = "Hakunamatata"
# print(len(name))
# print(name.replace('k','s'))
# print(name.replace('a','p'))

# name = input("What is your good name?")
# age = input("What is your age?")
# new_age = int(age) + 7
# print("Your age at 2030 is" + " " + str(new_age) )
# print(f"Your age is {new_age}")


# age = int(input("What is your age"))
# new_age = age + 7
# print(f"age is {new_age}")

# name = input("Enter your name: ")
# gender = input("Enter your Gender(male, female, others):").lower

# if gender == "male":
#     print(f"Hello {name} sir, How can i help you?")

# elif gender == "female":
#     print(f"Hello {name} mam, How can i help you")

# elif gender == "others":
#     print(f"Chal be chakke")

# else:
#     print(f"Wrong input hai bhai")

# import datetime

# current_year = str(datetime.datetime.now().date())

# print(f"The current year is {current_year}")

# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# gender = input("Enter Your Gender (Male, Female, Others): ").lower()

# if gender == "male":
#     print(f"Hello {name} sir, How's your day going on?")

# elif gender == "female":
#     print(f"Hello {name} Ma'am, How can I help you?")

# elif gender == "others" or gender == "other":
#     print(f"Hello {name}, How are You?")

# else:
#     print("Wrong Input please Enter your Gender correctly")


# import datetime
# current_year = (datetime.datetime.now().date())
# current_time = (datetime.datetime.now().time())
# print(f"The current date is {current_year}" )
# print(f"the current time is {current_time}")


# import datetime
# current_date = datetime.datetime.now().date()
# day_of_weeks = current_date.weekday()
# weekdays = "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"

# weekdays_name = weekdays[day_of_weeks]

# print(f"Today is {weekdays_name}")



# import random
# Your_name = input("Enter Your Name: ")
# dob = input("Your Date of Birth: ")
# Crush_name = input("Enter Your Crush's Name: ")
# dob2 = input("Enter your Crush's DOB: ")
# percentage = random.randint(40, 100)

# print(f"{Your_name} and {Crush_name} have a love percentage of {percentage}%")



# your_name = input("Enter Your Name: ")
# crush_name = input("Enter Your crush's name: ")
# part = len(crush_name)
# Whole = len(your_name)

# percentage = (part)/(Whole)*100
# print(f"{your_name} and {crush_name} has a love percentage of {percentage}")

# print("Check Your Eligibility to Vote")
# name = input("Enter your name: ")
# age = int(input("Enter Your age: "))

# if age >= 18:
#     print("Congrats, You are eligible to vote")

# else:
#     print("Sorry, You are not eligible to vote.")
#     print(f"Check again after {18 - age} Years.")



# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# operators = input("Enter operators(+ , - , / , * , % ): ")

# if operators == "+":
#     print(first + second)

# elif operators == "-":
#     print(first - second)

# elif operators == "/":
#     print(first / second)

# elif operators == "*":
#     print(first * second)

# elif operators == "%":
#     print(first % second)

# else:
#     print("invalid operation")


# for numbers in range(0,101):
#     print(numbers)


# i = 1
# while i <= 10:
#     print(i * "*")
#     i = i + 1

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 5
# while i >= 0:
#     print(i * "*")
#     i = i - 1


# for bro in range(10):
#     print(bro)
    



import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    random_number = random.randint(1, 100)
    guesses = 0
    max_guesses = 10

    while guesses < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guesses += 1

        if guess < random_number:
            print("Too low. Try again.")
        elif guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {guesses} attempts.")
            break

    else:
        print(f"Sorry, you're out of guesses. The correct number was {random_number}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    guess_the_number()
