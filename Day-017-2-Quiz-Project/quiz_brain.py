class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0


    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        correct_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_reply = input(f"Q.{self.question_number}: {current_question} (True/False)?:")
        if user_reply.lower() == correct_answer.lower():
            print(f"Correct. Your score is {self.score}/{len(self.questions_list)}.")
            self.score += 1
        else:
            print(f"Wrong. Your score is {self.score}/{len(self.questions_list)}.")
        print(f"The correct answer is : {correct_answer}")

    def roll_questions(self):
        while self.question_number < len(self.questions_list):
            self.next_question()
