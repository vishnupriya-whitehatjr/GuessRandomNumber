import random
number = random.randint(1, 9)
chances = 0
print("")
print("Guess a number between 1 to 9, You have 5 chances!!, Try your luck!")
while chances < 5:
    guess = int(input("Enter your guess number: "))
    if guess == number:
        print("BINGO! You guessed it right!!")
        break
    elif guess < number:
        print("Guess is low. Try Again!")
    else:
        print("Guess is high. Try Again!")
    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)