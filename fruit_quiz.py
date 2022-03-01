from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "What is 5 X 1,000,000 = ?\n(a) 5,000,000\n(b) :-(\n(c) 100\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a")
]

def run_test(questions_list):
    score = 0
    for q in questions_list:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct!")


run_test(questions)
