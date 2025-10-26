






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
# case
# spaces
# punctuation !"#$%&'()*+,-./:;<=>?@[\\]^_{|}~.
# is_palindrome("A man, a plan, a canal: Panama")  # True
# is_palindrome("No lemon, no melon")              # True
# =========================================================================================================
# Number guessing! Codewithmosh.
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
