#menu interface 
print("="*25)
print("Random number game")
print("select a number between 1 to 10")
print("see how many tries you need")
print('='*25)

#import module 
import random as rand

#initialise values 
secret_number = count = 0 

#range for secret random number 
secret_number = rand.randint(1,10)

#actual game 
go = True

while go :
    guess = input("guess a number between 1 to 10: ")
    if guess == secret_number :
        print("your guess is correct!")
        count += 1 
        print(f"number of tries --{count}")
        print("thank you for playing!")
        break
    elif guess < secret_number :
        print("your guess was too low, try again")
        count += 1
    elif guess > secret_number :
        print("yor guess is too high, try again")
    