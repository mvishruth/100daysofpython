#TODO 1 asking the question
class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0


  def still_has_question(self):
    return self.question_number < len(self.question_list)


  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False):")
    self.check_answer(user_answer, current_question.answer)

  def check_answer(self, user_answer, current_answer):
    if  user_answer.lower() == current_answer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("That's Wrong:")
    print(f"The Correct Answer was: {current_answer}.")
    print(f"Your Current score is {self.score}/{self.question_number}.")



#TODO 2 checking if the answer was correct

#TODO 3 checking if we'r at the end of the quiz