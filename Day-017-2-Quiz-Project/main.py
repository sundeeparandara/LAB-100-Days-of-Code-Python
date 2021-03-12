from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
#quiz.next_question()
quiz.roll_questions()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score} / {len(quiz.questions_list)}.")