def sum_even(lst):
    return sum(num for num in lst if num % 2 == 0)

print(sum_even([1, 2, 3, 4, 5, 6]))
