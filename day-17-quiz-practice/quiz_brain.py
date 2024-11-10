#TODO asking the questions
#TODO checking if answer is correct
#TODO checking if we are at the end of quiz

class QuizBrain:

  def __int__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

    def next_question():
      question = self.question_list[self.question_number]
      current_question = question.text
      current_answer = question.answer

      user_input = input(f"Q {self.question_number} {question_list} True/False:")
      if user_input == current_answer:
        self.score += 1
        self.question_number =+1
      else:
        print(f"your answer is wrong, Ans is {current_answer}")








