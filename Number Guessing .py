import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))

while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter the number again: "))
    elif guess > n :
        print("Too High")
        guess = int(input("Enter the number again: "))
    else:
        break
print("You guessed the right number!")      