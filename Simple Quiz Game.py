questions = {
    "Capital of India?": "Delhi",
    "5 + 7 = ?": "12",
    "Python is ___ typed language.": "dynamically"
}

score = 0
for q, a in questions.items():
    ans = input(q + " ").strip().lower()
    if ans == a.lower():
        score += 1

print(f"Your Score: {score}/{len(questions)}")
