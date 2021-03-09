class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.questions_list = question_list


    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        correct_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_reply = input(f"Q.{self.question_number}: {current_question} (True/False)?:")