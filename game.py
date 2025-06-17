# game.py

import random

# Sample questions (category, question, answer, points)
questions = [
    ("Science", "What planet is known as the Red Planet?", "Mars", 100),
    ("History", "Who was the first president of the United States?", "George Washington", 100),
    ("Pop Culture", "Which movie features the character 'Jack Sparrow'?", "Pirates of the Caribbean", 200),
]

def ask_question(q):
    category, question, answer, points = q
    print(f"\nCategory: {category} — Worth {points} points")
    print(question)
    user_answer = input("Your answer: ").strip()
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return points
    else:
        print(f"Wrong! The correct answer was: {answer}")
        return 0

def main():
    print("Welcome to Jeopardy!")
    random.shuffle(questions)
    score = 0
    for q in questions:
        score += ask_question(q)
    print(f"\nGame over! Your total score: {score}")

if __name__ == "__main__":
    main()