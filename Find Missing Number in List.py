def find_missing(lst):
    n = len(lst) + 1
    total = n * (n + 1) // 2
    return total - sum(lst)

print(find_missing([1, 2, 4, 5]))  # Missing 3
