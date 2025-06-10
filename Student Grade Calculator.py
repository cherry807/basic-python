def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

marks = list(map(int, input("Enter 5 subject marks separated by space: ").split()))
print("Grade:", calculate_grade(marks))
