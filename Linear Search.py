def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))
