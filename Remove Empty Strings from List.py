def remove_empty_strings(lst):
    return [s for s in lst if s]

print(remove_empty_strings(["apple", "", "banana", "", "cherry"]))
