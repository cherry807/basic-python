from collections import Counter

def frequency(lst):
    return dict(Counter(lst))

print(frequency([1, 2, 2, 3, 3, 3, 4]))
