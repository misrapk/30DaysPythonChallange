import random

#welcome message
print("***Welcome to Number Guessing Game!***")

#get user name
name = input("Enter your Name: ")


#print instruction
print(f"Hello {name}, I am thinking a number which is between 1 and 20.\n You have 5 Guesses to guess the number!")

number = random.randint(1,20)

for guessCount in range(5):
    print(f"Round {guessCount +1}")
    guess = int(input("Take a Guess: "))
    
 
    if guess > number: 
        print("Your Guess is too HIGH! Try Again")
    elif guess<number:
        print("Your Guess is too LOW! Try something Higher!")
    else:
        break


if guess==number: 
    print(f"Hurray! {name}. You guessed my number in {guessCount+1} guesses.")
else:
    print(f"GAME OVER! You Loose! \nMy number was {number}")
    