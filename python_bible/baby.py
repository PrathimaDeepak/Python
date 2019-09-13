from random import choice

questions = ["Why is the sky blue?: ", "Why is the moon so high?: ",
             "Why cant we fly?:"]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why? : ").strip().lower()

print("Oh.. okay")
