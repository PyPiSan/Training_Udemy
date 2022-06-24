from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for values in range(len(question_data)):
    questions = Question(question_data[values]['text'], question_data[values]['answer'])
    question_bank.append(questions)


p = QuizBrain(question_bank)


while p.still_has_question():
    p.nxt_quest()

print("The quiz is compeleted")

if p.score>6:
    print(f"Wow, your score is {p.score}/{p.question_number}")
else:
    print(f"Your score is {p.score}/{p.question_number}, Better Luck Next Time!")