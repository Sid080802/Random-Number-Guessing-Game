# import random module for generating random number.
import random

top_of_range = input("Type a range for generating random number : ")

# check the input is integer or not
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # check the entered number is greater than 0 or not
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()

else:
    print("Please type a number next time. ")
    quit()

# declare a range for generating the number.
random_number = random.randint(1, top_of_range)

# declare for counting the number of guesses
guesses = 0

while True:
    guess_number = input("Make a guess: ")
    # incrementing the guess value
    guesses += 1

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please type a number ")
        continue

    # check the entered number or generated number is same or not.
    if guess_number == random_number:
        print("you got it correct! ")
        break

    # give the hint for user, so they can predict entered guess is greater or less from generated number
    elif guess_number < random_number:
        print("You were below the number")
    else:
        print("you were above the number")

print("You successfully guess number in", guesses, "guesses")
