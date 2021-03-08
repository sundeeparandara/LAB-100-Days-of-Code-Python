from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

print(question_bank[0].text)
print(question_bank[0].answer)