def sum_nested(lst):
    return sum(sum(inner) for inner in lst)

print(sum_nested([[1, 2], [3, 4], [5]]))
