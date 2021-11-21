from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # all 10 questions are passing in this class one by one
    new_question = Question(question_text, question_answer)
    # and gets append in list in (self.) format pattern
    question_bank.append(new_question)

# object activating 10 questions to get use in the program
quiz = QuizBrain(question_bank)
# passing object of one class into another class
quiz_ui = QuizInterface(quiz)

# while loop can not operate with mainloop
# while quiz.still_has_questions():
#     quiz.next_question()
