# Py-Quizzler

This program asks you 10 random questions on Tkinter window, in boolean format, so it's like U.I Quiz game.

data.py: here we make request to an API, to give us questions, based on parameters we provide, than converts it in json format, saves all 10 questions, in
question_data, which is a list of dicts, and every dict is a separate question.

we extract, questions and answers from all the dicts, in main.py through for loop, saves it in question_bank list after passing each of them through a class of question_model
which allows us to save them in a (self.) format.

quiz_brain: here we pass the question_bank, it has methods like still_have_questions() which checks whether it still has some questions or not, next_question() which picks the
next question to show on screen, check_answer which checks our answers.

we pass entire QuizBrain class to ui.py in QuizInterface class,

ui.py: in initiating method it sets up a tkinter U.I and calls the next_question method in the end and after calls it window.mainloop() which makes it repeatative,
get_next_question, checks whether there's still questions left to ask than calls next_question method to pick the question and displays it on screen, otherwise just 
shows the end message and score.

than we have True and False button which triggers correct and wrong func respectively, passes our response to check_answer, which returns true or false based on whether
we were right or wrong.

than we have feedback func which changes color of canvas based on whether we were right or wrong.
