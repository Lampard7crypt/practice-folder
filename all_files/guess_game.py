min_value = int(input("Enter the lowest number you want to guess: "))
max_value = int(input("Enter the highest number you want to guess: "))
from random import randint
try:
    while True:
        print("type nothing to quit")
        number = int(input("Guess: "))
        guess = randint(min_value, max_value)
        print(guess)
        if number > guess:
            print("too high")
        elif number < guess:
            print("Too low")
        
        else:
            print("Correct")
            break
except ValueError:
    pass
print("You escaped my infinite tsukuyomi!")
