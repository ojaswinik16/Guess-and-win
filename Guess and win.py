import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a positive number')
        quit()
else:
    print('Please enter a number')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("guess the number between 1-25: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Enter a number.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break

if guesses<3:
    print("you won")
else:
    print("better luck next time")
