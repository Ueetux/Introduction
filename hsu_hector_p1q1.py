import time
from rich import print

# Quiz has 5 questions the user will answer.
# It will keep track of score and give
# a final result.

# Introduction
print("Welcome to QwiZ.")
time.sleep(2)
print("Good luck!")

# Create a list of questions
questions = [
    ["How old am [bold italic green]I[/bold italic green]? ", "16"],
    ["When was the first time i drove a [bold italic green]car[/bold italic green]?", "don't remember"],
    ["What is my favourite food?", "Mitarashi Dango"],
]

# For each question, print it out and ask the user to answer
for question in questions:
    # Print the question
    print(question[0])

    # Get the user's answer
    user_answer = input().lower().strip(",..?!")

    neg_answers = [
        ["I cant beleive you didntknow that about me how could you."],
        ["What you got it wrong?! I thought we were freinds bro."]
    ]
   # See if they're correct
    if user_answer == question[1]:
        print("dame u got it right! good job!")
    else:
        print("")
