from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# converting list of dictionary (question_data) into list of objects.
question_bank = []
for que in question_data:
    question = Question(txt = que["text"], ans = que["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")