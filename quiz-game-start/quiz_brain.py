from question_model import Question


class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def nxt_quest(self):
        new_question = self.question_list[self.question_number]
        self.question_number+=1
        usr_ans = input(f"Q.{self.question_number}: {new_question.text}(True/False): ")
        correct_ans = new_question.ans
        self.check_answer(usr_ans, correct_ans)

    def check_answer(self, usr_ans, correct_ans):
        if usr_ans == correct_ans:
            self.score+=1
            print(f"You got it right.")
        else:
            print(f"You got it wrong.")

        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")