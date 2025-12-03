# Ninety-nine bottles of milk on the wall, ninety-nine bottles of milk. take one down pass it around, ninety-eight bottles of milk on the wall.
import inflect
p = inflect.engine()
number = int(input("Enter a number: "))
for i in range(number, 0, -1):
    if i > 1:
        print(f"{(p.number_to_words(i)).capitalize()} bottles of milk on the wall, {p.number_to_words(i)} bottles of milk. take one down pass it around, {p.number_to_words(i-1)} bottles of milk on the wall.")
        i -= 1
        continue
    print("One bottle of milk on the wall, one bottle of milk. Take it down pass it around, no more bottles of milk on the wall.")
