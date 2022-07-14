import random
"""
Code inspiration and game idea taken from Tech With Tim youtube channel
"""
top_of_range = input("Type a number: ")
"""
Sets out the number to be added to create the range for guesses
"""
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than o next time.')
        quit()
else:
    print('Please type a number')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
"""
This section allows the user to make a guess what they think the number is
and prevents any words or letters being guessed, only number
"""
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!" '\n')
        else:
            print("You were below the number" '\n')
"""
This section tells the user how many times it took them to guess the
correct answer
"""
print("You got it right in", guesses, "guesses")
