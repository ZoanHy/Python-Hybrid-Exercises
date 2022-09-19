import tkinter
from quiz_brain import QuizBrain
from PIL import ImageTk, Image

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        # row 0
        self.label_score = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.label_score.grid(row=0, column=1)

        # row 1
        self.canvas = tkinter.Canvas(height=250, width=300, background="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="ABC", font=("Arial", 16, "italic"),
                                                     fill=THEME_COLOR)
        image_true = ImageTk.PhotoImage(Image.open("images/true.png"))
        image_false = ImageTk.PhotoImage(Image.open("images/false.png"))

        # row 2
        self.button_true = tkinter.Button(image=image_true, highlightthickness=0, command=self.check_answer_true)
        self.button_true.grid(row=2, column=0)

        self.button_false = tkinter.Button(image=image_false, highlightthickness=0, command=self.check_answer_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
