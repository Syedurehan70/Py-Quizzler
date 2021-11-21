from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    
    # now we can use all the methods of QuizBrain in this class
    def __init__(self, quiz_brain: QuizBrain):
        
        # we've assigned the object of another class to an attribute,
        self.quiz = quiz_brain
        
        # UI formation
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=270, bg="white", highlightthickness=0)
        
        # the width inside create_text won't allow the text to go out of canvas
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.correct, bd=0)
        self.true_button.grid(row=4, column=0)
        
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.wrong, bd=0)
        self.false_button.grid(row=4, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        
        if self.quiz.still_has_questions():
            
            # q_text saves the returning string from next_question method from QuizBrain, quiz method.
            q_text = self.quiz.next_question()
            
            # displays the question on screen
            self.canvas.itemconfig(self.question_text, text=q_text)
            
            # this will enabled the buttons and we will be  able to press them again
            self.button_enabled()
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the End, of the Quiz\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

            # this will disable the buttons and we will not be  able to press them again
            self.button_dissabled()

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # delay of 1 sec, than running get_next_question again
        self.window.after(1000, self.get_next_question)

    def button_enabled(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def button_dissabled(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
