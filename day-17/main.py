from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dictionary in question_data:
    question_bank.append(Question(dictionary['text'], dictionary['answer']))

quiz = QuizBrain(question_bank)

while quiz.stil_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
