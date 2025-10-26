# rock paper scissors game!
import random
def rockpaperscissors():
	computer, person = 0, 0
	r, p, s = "🪨", "📃", "✂️"
	lst = [r, p, s]
	while computer + person < 5:
		c_choice = random.choice(lst)
		while True: # Checks if it's r, p or s, then assigns them to the emoji.
			choice = input("r/p/s: ").lower()
			if choice == 'r':
				choice = r
				break
			if choice == 'p':
				choice = p
				break
			if choice == 's':
				choice = s
				break
			else:
				continue
		
		# Checks who the winner is and adds one to their score.
		if c_choice == r and choice == p:
			person += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('You win this round!')
		if c_choice == p and choice == s:
			person += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('You win this round!')
		if c_choice == s and choice == r:
			person += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('You win this round!')
		if c_choice == choice:
			print(f'You chose {choice}, computer chose {c_choice}')
			print('Draw')
		if choice == r and c_choice == p:
			computer += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('Computer wins this round!')
		if choice == p and c_choice == s:
			computer += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('Computer wins this round!')
		if choice == s and c_choice == r:
			computer += 1
			print(f'You chose {choice}, computer chose {c_choice}')
			print('Computer wins this round!')
		
		# check is the user wants to play again.
		decide = input("Would you like to try again(y/n) ")
		if decide == 'y':
			continue
		if decide == 'n':
			break
	
	print(f'You won {person} times, computer won {computer} times!')
	if person > computer:
		print("Congrats! You win!")
	if person == computer:
		print("Draw!")
	else:
		print('Computer wins!')

rockpaperscissors()





# =========================================================================================================
# Write a function to recursively reverse a nested list.
# reverse_nested([1, [2, [3, 4], 5]])  # Output: [ [5, [4, 3], 2], 1 ]
def reverse_nested(lst):
    if isinstance(lst, list):
        return [reverse_nested(item) for item in reversed(lst)]
    else:
        return lst

# =========================================================================================================
# Write a function that returns True if a string is a palindrome, ignoring:
# - case
# - spaces
# - punctuation !"#$%&'()*+,-./:;<=>?@[\\]^_{|}~.
# is_palindrome("A man, a plan, a canal: Panama")  # True
# is_palindrome("No lemon, no melon")              # True
# =========================================================================================================
# Number guessing!
import random
def guess():
	lst = []
	while True:
		try:
			a = int(input("Minimum number you want: "))
			b = int(input("Maximum number you want: "))
		except ValueError:
			print("Not an integer!")
			continue
		randnum = random.randint(a, b)
		counter = 0
		while counter < 10:
			guess = int(input("Guess: "))
			if guess > randnum:
				counter += 1
				print("Too high!")
				continue
			if guess < randnum:
				counter += 1
				print("Too low!")
				continue
			if guess == randnum:
				lst.append(counter)
				print(f"You are correct! You guessed the number in {counter} attempts!")
				break
		if counter > 9:
			print(f"You have failed 10 times, the answer was {randnum}!")
		while True:
			try_again = input("Would you like to try again(Y/N) ").lower()
			if try_again == "y":
				break
			if try_again == "n":
				print(f"Minimum tries to get it right was {min(lst, default=0)}")
				return
			else:
				continue
# =========================================================================================================
