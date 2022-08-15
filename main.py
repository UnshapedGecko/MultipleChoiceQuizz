from Question import Question

question_prompts = [
  "What city is the captiol of the USA?\n(a) NewYork\n(b) Washington DC\n(c) Los Angeles\n",
  "What is the longest river in the USA?\n(a) Missouri River\n(b) Yukon River\n(c) Red River\n",
  "Who is present USA president?\n(a) Donald Trump\n(b) Barack Obama\n(c) Joe Biden\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)