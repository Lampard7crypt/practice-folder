# ========================================================================================
# Learn more about Python Sort and sorted functions!
def sort_by_age(s: list):
    return sorted(s, key=lambda item: item[1])

print(sort_by_age([('Alice', 30), ('Bob', 25), ('Eve', 35)]))
