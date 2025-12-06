# ========================================================================================
# Learn more about Python Sort and sorted functions!
def sort_by_age(s: list):
    return sorted(s, key=lambda item: item[1])

# print(sort_by_age([('Alice', 30), ('Bob', 25), ('Eve', 35)]))

def count_vowels(s: str) -> str:
    return len([letter for letter in s if letter in ['a', 'e', 'i', 'o', 'u']])

# print(count_vowels("vowel"))



