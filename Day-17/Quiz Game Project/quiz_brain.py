class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
        # if self.question_number < len(self.questions_list):
        #     return True
        # else:
        #     return False

    def check_answer(self, ans, right_ans):
        if ans == right_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {right_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        your_answer = input(f"\nQ.{self.question_number}: {question.text} (True/False)?: ").strip().lower()
        self.check_answer(ans = your_answer, right_ans = question.answer)