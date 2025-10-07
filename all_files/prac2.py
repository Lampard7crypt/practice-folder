list1 = ['a', 'b', 'c', 'd', 'e', 'A']
vowel = "aeiou"
for letter in list1[:]:
    if letter.lower() in vowel:
        list1.remove(letter)
    else:
        print(letter, end='')