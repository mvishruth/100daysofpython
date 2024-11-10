from question_model import Question
from quiz_brain import QuizBrain
from data import question

#TODO 1 Create a question and Answer attribute new_question object constructor code will add to question attribute



question_bank = []

for q in question_data:
  text = q["text"]
  answer = q["answer"]
  new_question = Question(text, answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(quiz.question_number)
